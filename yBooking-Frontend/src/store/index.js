import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      email: "",
      isLogin: false,
      keyword: ""
    };
  },
  mutations: {
    Email(state, email) {
      state.email = email;
    },
    isLogin(state, bool) {
      state.isLogin = bool;
    },
    keyword(state, keyword) {
      state.keyword = keyword;
    }
  },
  actions: {
    updateEmail(context, email) {
        context.commit('Email', email);
    },
    updateLogin(context, login) {
      context.commit('isLogin', login);
    },
    updateKeyword(context, keyword) {
      context.commit('keyword', keyword);
    }
  },
  modules: {
  }
});

export default store;
