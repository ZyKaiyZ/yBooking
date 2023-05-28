import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      email: "Hello",
      isLogin: false
    };
  },
  mutations: {
    Email(state, email) {
      state.email = email;
    },
    isLogin(state, bool) {
      state.isLogin = bool;
    }
  },
  actions: {
    updateEmail(context, email) {
        context.commit('Email', email);
    },
    updateLogin(context, login) {
      context.commit('isLogin', login);
    }
  },
  modules: {
  }
});

export default store;
