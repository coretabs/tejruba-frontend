import axios from 'axios'


const baseURL1 = 'http://localhost:8000';
const baseURL2 = 'http://127.0.0.1:8000';

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'

const simpleRequest = axios.create({
    baseURL: baseURL1,
    timeout: 1000,
    // headers: {'X-Custom-Header': 'foobar'}
  });

  const preflightedRequest = axios.create({
    baseURL: baseURL1,
    timeout: 1000,
    //headers: {'X-Custom-Header': 'foobar'}
  });

  const credentialsRequest = axios.create({
    baseURL: baseURL1,
    timeout: 1000,
    // headers: {'X-Custom-Header': 'foobar'}
  });

  simpleRequest.get('/')
    .then( function (response) {
        console.log(response.data);
        data = response.data;
    }).catch( function (error) {
        console.log(error);
        error = error;
});
