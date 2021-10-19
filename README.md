<p align="center">
  <img src="https://specnith.com/Home-files/assets/logo2.png" alt="Logo" width="480">

  <h2 align="center">SPEC NITH</h2>

  <p align="center">
    Official Codebase
    <br>
    <a href="https://github.com/spec-nith/spec-backend/issues">Report Bug</a>
    ·
    <a href="https://github.com/spec-nith/spec-backend/issues">Request Feature</a>
  </p>
</p>
<br>
<p align="center">
  <a href="https://github.com/spec-nith/spec-backend/graphs/contributors">
    <img alt="Contributors" src="https://img.shields.io/github/contributors/spec-nith/spec-backend.svg?style=for-the-badge" style="max-width:100%;">
  </a>
  <a href="https://github.com/spec-nith/spec-backend/network/members">
    <img alt="Forks" src="https://img.shields.io/github/forks/spec-nith/spec-backend.svg?style=for-the-badge" style="max-width:100%;">
  </a>
  <a  href="https://github.com/spec-nith/spec-backend/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/spec-nith/spec-backend.svg?style=for-the-badge" style="max-width:100%;">
  </a>
  <a href="https://github.com/spec-nith/spec-backend/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/spec-nith/spec-backend.svg?style=for-the-badge" style="max-width:100%;">
  </a>
</p>

## 📝 General Overview 

This repository contains all the source code for ***Django backend*** of the official website of Society for Promotion of Electronics Culture (SPEC), NIT Hamirpur from 2021 onwards. <!--SPEC is run under the aegis of Electronics and Communication Department of NITH and is renowned for conducting a national level hackathon [ELECTROTHON](https://specnith.com/electrothon.html) along with a plethora of workshops, competitions, guest talks and the annual technical fest - [SPECFEST](https://specnith.com/specfest2k21.html).-->

Visit the current official website of SPEC from [here](https://specnith.com/).

## ⚙️ Set-Up and Usage

- To  run the project, install all the dependencies:
  
  ```
  make install
  ```

- You can use ```make``` commands to perform various operations in your django project.
  
  - Start django server on port `8000`. You can customize it by editing `PORT` in `Makefile`:
    ```
    make run
    ```
    ```
    make runssl
    ```

  - Apply database migrations: 
    ```
    make migrate
    ```

  - Clear database records:
    ```
    make flush
    ```
    *Note: Media files will not be delewted using this command*

  - Update project requirements (useful for deployment)
    ```
    make freeze
    ```
    This command will add all your project dependencies to `etc/requirements.txt`, making it very easy for deployment.      

  
  - Check for proper formatting and import style using `black` and `isort`
    ```
    make format
    ```   

  - Running Django Testcases
    ```
    make test
    ```

  - Running black validation
    ```
    make check
    ```     





## 🎯  Contributing Guidelines
Contributions are what make the open source community such an amazing place to  learn, inspire and build experiences that are cherished for a lifetime.  Go ahead and follow these steps to contribute to the community.

- Fork this repository by clicking on   *Fork* button on the top right side.

- Clone your Fork to your local machine
  ```
  git clone [https://github.com/your-username/spec-frontend.git]
  ```
         
- Create your Feature Branch
  ```
  git checkout -b [branch-name]
  ```
         
- Make your changes and commit them
  ```
  git add . 
  git commit -m "Add some amazing feature" 
  ```

- To check the status
  ```
  git status
  ```
         
- And then push the changes to your forked repository
  ```
  git push origin [branch name]
  ```

- Click on the *New Pull Request* button at the top of your repository to create a new pull request from your forked repository.

- Wait for your PR review and merge approval.

- Don't forget to ⭐ this repository.
