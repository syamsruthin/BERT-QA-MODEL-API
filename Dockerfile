FROM python:3.7
COPY . /work_dir
WORKDIR /work_dir

#RUN apk add --update curl gcc g++ \
#    && rm -rf /var/cache/apk/*

#RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["python3"]
CMD ["app.py"]


