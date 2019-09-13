import axios from 'axios'

let $backend = axios.create({
  baseURL: 'https://tejruba1.herokuapp.com/api/',
  // timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  },

})

// Response Interceptor to handle and log errors
$backend.interceptors.response.use(function (response) {
    return response
  },
  function (error) {
    // eslint-disable-next-line
    console.log(error)
    return Promise.reject(error)
  })

$backend.$register = (user) => {
  return $backend.post(`accounts/registration/`, {
      username: user.name,
      email: user.email,
      password1: user.password,
      password2: user.password
    })
    .then(response => {
      console.log(response.data)
      return response.data
    })
}
export default $backend