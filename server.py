from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def index():
    # 模拟耗时io
    time.sleep(2)
    return 'hello'


if __name__ == '__main__':
    # 启动多线程模式
    app.run(threaded=True)
