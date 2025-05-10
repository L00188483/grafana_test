### Stackhawk CLI running in docker

##### Setup
* Paste your API key into: hawk_cli_docker.sh 
    - get an API key from: https://app.stackhawk.com/settings/apikeys
* make it executable: ```$ chmod +x hawk_cli_docker.sh```
* ensure you have a `stackhawk.yml` file in your current directory
    - go to: https://app.stackhawk.com/applications
    - click 'Add Application' and follow the wizard (skip the install step)
    - download the .yml file
    

##### Run cli
```bash
$ ./hawk_cli_docker.cli
```

##### View your scan
Go to: https://app.stackhawk.com/scans
