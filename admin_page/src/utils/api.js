import jwt from 'jwt-decode';
import axios from 'axios';

export default class {
  constructor (settings, store, prefixPath) {
    let api = axios.create(settings);
    api.interceptors.request.use(config => {
      config.headers = { Authorization: this.store.state.auth.accessToken };
      return config;
    });
    api.interceptors.response.use(this.handleSuccess, error => {
      return this.handleError(error);
    });
    this.api = api;
    this.store = store;
    this.settings = settings;
    this.prefixPath = prefixPath === '' ? store.getters['user/getActiveTenant'].tenant_id : prefixPath;
  }

  setPrefixPath (path) {
    this.prefixPath = path;
  }

  handleSuccess (response) {
    return response;
  }

  handleError (error) {
    this.store.commit('setLoading', false, { root: true });

    // An error occurred
    error.response = this.convertUnexpectedErrorScheme(error);

    // Unauthorized
    if (error.response.data.code === 401) {
      this.store.dispatch('auth/logout', error.response.data);
    }

    return Promise.reject(error);
  }

  convertUnexpectedErrorScheme (error) {
    // CORS
    if (error.response === undefined) {
      return {
        data: {
          code: 500,
          detail: error.message
        }
      };
    }

    // 想定のschemeの場合
    if (error.response.data.hasOwnProperty('code')) {
      return error.response;
    }

    // Internal Server Error
    if (error.response.status >= 500) {
      return {
        data: {
          code: error.response.status,
          detail: error.response.data.message
        }
      };
    }

    return error.response;
  }

  getToken (username, password) {
    axios.interceptors.response.use(
      response => response,
      error => {
        this.store.commit('setLoading', false, { root: true });

        // An error occurred
        error.response = this.convertUnexpectedErrorScheme(error);

        return Promise.reject(error);
      }
    );

    return axios
      .post(`${this.settings.baseURL}/support_member/login`, {
        username: username,
        password: password
      })
      .then(res => {
        return new Promise((resolve, reject) => {
          if (res.status !== 200) {
            return reject(res.response);
          } else {
            return resolve(res.data);
          }
        });
      })
      .then(data => {
        let decodedToken = jwt(data.token.access_token);
        this.store.commit('auth/setAccessToken', data.token.access_token, { root: true });
        this.store.commit('auth/setRefreshToken', data.token.refresh_token, { root: true });
        this.store.commit('auth/setDecodedToken', decodedToken, { root: true });
        this.store.commit('user/setScope', decodedToken.scope, { root: true });
        this.store.commit('user/setTenants', data.tenants, { root: true });
      });
  }

  discardToken () {
    return axios
      .get(`${this.settings.baseURL}/support_member/logout`, {
        headers: { Authorization: this.store.state.auth.accessToken }
      })
      .catch(() => {});
  }

  isNecessaryRefresh () {
    const expirationTime = this.store.state.auth.decodedToken.exp * 1000; // msec換算
    const issuedAtTime = this.store.state.auth.decodedToken.iat * 1000; // msec換算
    const now = Date.now();

    const availableTime = expirationTime - issuedAtTime; // 有効時間
    const elapsedTime = now - issuedAtTime; // 経過時間
    const threshold = this.settings.tokenRefreshThreshold;

    return elapsedTime / availableTime > threshold;
  }

  fetchToken () {
    if (this.isNecessaryRefresh()) {
      return axios
        .post(`${this.settings.baseURL}/support_member/refresh`, {
          access_token: this.store.state.auth.accessToken,
          refresh_token: this.store.state.auth.refreshToken
        })
        .then(res => {
          return new Promise((resolve, reject) => {
            if (res.status !== 200) {
              return reject(res.response);
            } else {
              return resolve(res.data);
            }
          });
        })
        .then(data => {
          let decodedToken = jwt(data.access_token);
          this.store.commit('auth/setAccessToken', data.access_token, { root: true });
          this.store.commit('auth/setDecodedToken', decodedToken, { root: true });
          this.store.commit('user/setScope', decodedToken.scope, { root: true });
        });
    } else {
      return Promise.resolve;
    }
  }

  async get (path, payload = {}) {
    await this.fetchToken();
    return this.api.get(`${this.prefixPath}${path}`, { params: payload });
  }

  async delete (path) {
    await this.fetchToken();
    return this.api.delete(`${this.prefixPath}${path}`);
  }

  async patch (path, payload) {
    await this.fetchToken();
    return this.api.patch(`${this.prefixPath}${path}`, payload);
  }

  async post (path, payload) {
    await this.fetchToken();
    return this.api.post(`${this.prefixPath}${path}`, payload);
  }
}
