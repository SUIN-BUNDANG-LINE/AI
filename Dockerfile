FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt /tmp/
RUN python3 -m pip install --upgrade pip -q
RUN python3 -m pip install -r /tmp/requirements.txt -q

COPY .env ${LAMBDA_TASK_ROOT}
COPY ./app/ ${LAMBDA_TASK_ROOT}/app/

CMD [ "app.main.Handler" ]