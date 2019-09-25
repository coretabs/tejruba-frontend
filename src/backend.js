import axios from 'axios'

var localBaseUrl = 'http://localhost:8000/api/';
var remoteBaseUrl = 'https://tejruba1.herokuapp.com/api/';

let $backend = axios.create({
  // baseURL: localBaseUrl,
  // timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  },

})

$backend.defaults.baseURL = localBaseUrl;

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