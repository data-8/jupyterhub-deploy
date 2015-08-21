FROM jupyter/systemuser

# Install nbgrader
RUN pip3.4 install git+git://github.com/jhamrick/nbgrader.git@compmodels

# Install terminado
RUN pip2.7 install terminado
RUN pip3.4 install terminado

# Install datascience
RUN pip2.7 install datascience==0.3.0
RUN pip3.4 install datascience==0.3.0

RUN pip2.7 install notebook-ok-extension
RUN pip3.4 install notebook-ok-extension

RUN pip2.7 install okpy
RUN pip3.4 install okpy

# /usr/local/lib/python3.4/dist-packages/IPython/html/static/custom/
#ADD https://raw.githubusercontent.com/dsten/notebook/master/notebook/static/custom/dsten.css /usr/local/lib/python3.4/dist-packages/IPython/html/static/custom/dsten.css
#ADD https://raw.githubusercontent.com/dsten/notebook/master/notebook/static/custom/dsten.css /srv/ipython/IPython/html/static/custom/dsten.css

#ADD https://raw.githubusercontent.com/dsten/notebook/master/notebook/static/custom/dsten.js /usr/local/lib/python3.4/dist-packages/IPython/html/static/custom/dsten.js
#ADD https://raw.githubusercontent.com/dsten/notebook/master/notebook/static/custom/dsten.js /srv/ipython/IPython/html/static/custom/dsten.js

#RUN sed -i "s/.*custom\/custom.*/    \'custom\/dsten\',\n&/" /usr/local/lib/python3.4/dist-packages/IPython/html/static/notebook/js/main.js
