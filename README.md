It simply my answers to CtCI (Cracking the Coding Interviews book by Gayle Laakmann McDowell)

#How to run python inside disposable Docker container
Step 1 - Build docker image
docker build -t kd/mypy:withtmux .

Step 2 - Just run it - Mount program directory and run disposable container in interactive mode
docker run --rm -it -v $(PWD):/data kd/mypy:withtmux /bin/bash
