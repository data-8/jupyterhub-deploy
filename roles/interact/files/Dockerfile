FROM python:3

RUN pip install flask requests webargs

RUN git clone https://github.com/dsten/DS8-interact /srv/interact

WORKDIR /srv/interact

ENTRYPOINT ["python", "run.py"]
CMD ["--production"]
