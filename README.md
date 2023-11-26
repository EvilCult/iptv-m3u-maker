# F.U.N.R

This project is designed to quickly start a web service based on Flask and deployed using Nginx+uWSGI. The client interface is developed using React Native.

## Usage

After downloading the files, modify the following files:

- Modify the filename of **Serv** in the Projects path to the project name of your application. Also modify **'WORKDIR'** in **dockerfile_python** file.
- Modify the **'access_log'** and **'error_log'** paths in /**Nginx/cfg/project.conf**. Also modify the directory name under **/Nginx/log**.
- Modify **'MYSQL_PWD'** and **'REDIS_PWD'** in the **.env** file in the root directory to prevent weak password vulnerabilities.

Execute the following command in the root directory: 
> docker-compose up -d

Start the project.

Good Luck!