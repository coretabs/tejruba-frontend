import $backend from '@/backend';
export default {
  register({ commit }, user) {
    return new Promise((resolve, reject) => {
      $backend.$register(user).then(response => {
          resolve(response)
        })
        .catch(err => {
          reject(err)
        })
    })
  },
}