# OpenDictionaryAPI 🌟📚

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](#contributing)
[![Issues](https://img.shields.io/github/issues/SH20RAJ/OpenDictionaryAPI)](https://github.com/SH20RAJ/OpenDictionaryAPI/issues)
[![Forks](https://img.shields.io/github/forks/SH20RAJ/OpenDictionaryAPI?style=social)](https://github.com/SH20RAJ/OpenDictionaryAPI/fork)
[![Stars](https://img.shields.io/github/stars/SH20RAJ/OpenDictionaryAPI?style=social)](https://github.com/SH20RAJ/OpenDictionaryAPI/stargazers)
[![NPM Version](https://img.shields.io/npm/v/opendictionaryapi)](https://www.npmjs.com/package/opendictionaryapi)
[![Visitors](https://api.visitorbadge.io/api/combined?path=https%3A%2F%2Fgithub.com%2FSH20RAJ%2FOpenDictionaryAPI&labelColor=%232ccce4&countColor=%23dce775&style=flat)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2FSH20RAJ%2FOpenDictionaryAPI)

**OpenDictionaryAPI** is a free and open-source API that provides access to word definitions, synonyms, antonyms, pronunciations, and more. 🧑‍💻 Perfect for developers and language enthusiasts who want to integrate dictionary data into their applications. 🚀

---

## Features 🌟
- 📖 **Word Definitions**: Accurate and detailed meanings for words.
- 🔄 **Synonyms and Antonyms**: Explore related words and opposites.
- 🎧 **Pronunciations**: Access audio pronunciations to improve your skills.
- 🌍 **Multiple Languages**: Look up words in different languages.
- ⚡ **Fast & Reliable**: Built to deliver fast and consistent responses.

---

## Installation & Usage (NPM) 🚀

Install the package from [npm](https://www.npmjs.com/package/opendictionaryapi):

```bash
npm i opendictionaryapi
```

### Example Usage:
```javascript
const OpenDictionaryAPI = require("opendictionaryapi");

OpenDictionaryAPI.search('hi', 'en')
  .then(results => {
    console.log(results);
  })
  .catch(error => {
    console.log(error);
  });
```

### Results Example:
```json
[
  {
    "word": "hello",
    "phonetics": [
      {
        "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3",
        "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=75797336",
        "license": {
          "name": "BY-SA 4.0",
          "url": "https://creativecommons.org/licenses/by-sa/4.0"
        }
      }
    ],
    "meanings": [
      {
        "partOfSpeech": "noun",
        "definitions": [
          {
            "definition": "\"Hello!\" or an equivalent greeting."
          }
        ]
      }
    ],
    "sourceUrls": [
      "https://en.wiktionary.org/wiki/hello"
    ]
  }
]
```

### Error Example:
```json
{
  "title": "No Definitions Found",
  "message": "Sorry pal, we couldn't find definitions for the word you were looking for.",
  "resolution": "You can try the search again at a later time or head to the web instead."
}
```

---

## Direct API Usage 🔗

You can also directly fetch word data via the URL:

```plaintext
https://www.jsdelivr.com/package/gh/SH20RAJ/OpenDictionaryAPI/data/english/{word}.json
```

### Example:
Fetch data for the word "hello":
```plaintext
https://cdn.jsdelivr.net/gh/SH20RAJ/OpenDictionaryAPI/data/english/hello.json
```

---

## Installation & Development 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/SH20RAJ/OpenDictionaryAPI.git
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the server:
   ```bash
   npm start
   ```

---

## Contributing 🤝
We welcome contributions from the community! 🛠️ To get started:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Added new feature"`.
4. Push to your branch: `git push origin feature-name`.
5. Submit a pull request. 🎉

---

## License 📝
This project is licensed under the [MIT License](LICENSE).

---

## Contact ✉️
For questions or support, please reach out via [Issues](https://github.com/SH20RAJ/OpenDictionaryAPI/issues).

---

⭐ **If you find this project helpful, give it a star!** ⭐
