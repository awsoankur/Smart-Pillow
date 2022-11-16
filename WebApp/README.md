### Install nvm
Open a terminal and then type:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```
```
source ~/.bashrc
```
Run this command succesfully ( You might also need to install curl )

### Verify installation - should output nvm if successful
Now close the terminal and open a new terminal
```bash
command -v nvm
```

### Install Node 16.13.0
```bash
nvm install 16.13.0
```
```bash
nvm alias default 16.13.0
```
```bash
nvm use 16.13.0
```
### Install yarn
```bash
npm install --global yarn
```

### Install concurrently
```bash
npm install --global concurrently
```

### Install dependencies for the project
Change the working directory to the project directory i.e. WebApp
Run the following command to install the dependencies.
```bash
yarn
```

### Run the project
Run the following command to run the project to **localhost**
```bash
yarn dev
```