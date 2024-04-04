const express = require("express");
const cheerio = require("cheerio");
const axios = require("axios"); // loading in all the packaghes
const fs = require("fs");
const readline = require("readline");
const filePath = "output.txt";
const craigslist = require("./craigslist");

const app = express(); // starting up express
const startedUp = false;

const hashTable = new Map();
console.log("==================================");

craigslist
  .getPostings()
  .then((postings) => {
    console.log("Received postings:");
    let dataToWrite = "";
    for (let i = 0; i < postings.length; i++) {
      dataToWrite += postings[i].title + " " + postings[i].location + "\n";
    }

    fs.writeFile(filePath, dataToWrite, (err) => {
      if (err) {
        console.error("Error writing to file:", err);
      } else {
        console.log("Data written to file successfully.");
      }
    });

    for (let i = 0; i < postings.length; i++) {
      data = postings[i];
      const key = djb2Hash(data.title + " " + data.location);
      console.log(key);
      if (key in hashTable) console.log("=== \n collision \n ===");
      hashTable.set(key, data.title + " " + data.location);
    }
  })
  .then(() => {
    setInterval(() => {
      console.log("reapeating");
      craigslist.getPostings().then((postings) => {
        for (let i = 0; i < postings.length; i++) {
          const post = postings[i];
          const entry = post.title + " " + post.location;
          const key2 = djb2Hash(entry);
          console.log(entry);
          if (hashTable.has(key2)) {
            console.log("There is a collision in updateing the database.");
          } else {
            console.log("Found new posting while updateing the database.");
            console.log(key2);
            hashTable.set(key2, entry);
            const accountSid = "AC88012deda467d900f4b9e12f01d35c5e";
            const authtoken = "d19f04b0fc6f0b44a2216e9a56c62010";

            const client = require("twilio")(accountSid, authtoken);
            const keywords = [
              "take all",
              "clothes",
              "estate",
              "free",
              "shoe",
              "shirts",
              "pants",
              "jacket",
              "sweater",
            ];

            const regex = new RegExp(keywords.join("|"));

            if (regex.test(entry.replace(/_/g, " "))) {
              console.log("Keywords found!");

              client.messages
                .create({
                  to: "+17608282870",
                  from: "+18777937056",
                  body: "New Craigslit Free Posting \n\n" + entry,
                })
                .then((message) => console.log(message.sid));
            } else {
              console.log("Keywords not found.");
            }
          }
        }
      });
    }, 60000);
  })
  .catch((error) => {
    console.error("An error occurred:", error);
  });

function djb2Hash(str) {
  let hash = 5381;
  for (let i = 0; i < str.length; i++) {
    hash = (hash * 33) ^ str.charCodeAt(i);
  }
  return hash >>> 0; // Ensure positive 32-bit integer hash value
}

console.log("Finished");
console.log("==================================");

console.log("Finished");

app.listen(3000, () => console.log("program is running ... ")); // listending to port 3000
