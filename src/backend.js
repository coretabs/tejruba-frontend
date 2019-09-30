import axios from 'axios'

const localBaseUrl = 'http://localhost:8000/api/';
const remoteBaseUrl = 'https://tejruba1.herokuapp.com/api/';
const CSRF_COOKIE_NAME = 'csrftoken';
const CSRF_HEADER_NAME = 'X-CSRFToken';

let $backend = axios.create({
  baseURL: localBaseUrl,
  // timeout: 5000,
  // headers: {
  //   'Content-Type': 'application/json',
  //   'Access-Control-Allow-Origin': '*'
  // },
  xsrfCookieName: CSRF_COOKIE_NAME,
  xsrfHeaderName: CSRF_HEADER_NAME
})

$backend.defaults.baseURL = remoteBaseUrl;

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
  console.log(user);
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