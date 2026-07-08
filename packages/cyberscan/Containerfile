FROM alpine 

RUN apk add --no-cache fish python3 git
RUN /usr/bin/fish -c "set -U fish_greeting"
WORKDIR /root
RUN git clone https://gitea.com/cyberwarn/cyberscan
RUN apk del git
WORKDIR /root/cyberscan
RUN python3 -m venv venv && ./venv/bin/pip install -r packages.txt
RUN echo "source /root/cyberscan/venv/bin/activate.fish" > /root/.config/fish/config.fish
CMD ["fish"]
