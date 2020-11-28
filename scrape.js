const axios = require('axios');
const fs = require('fs');

const URL = "https://content.wdl.org/10096/service/thumbnail/1431369762/1024x1024/1/";
var ftype = ".jpg";

var i = 1;

axios.get(URL + i.toString() + ftype)
  .then(function (response) {
    // handle success
    fs.writeFileSync("img.jpg", response.data, function(err) {
        if(err) {
            return console.log(err);
        }
        console.log("The file was saved!");
    });

    // Object.keys(response.data).forEach(function(key) {
    //   console.log(key);
    // });
  });
