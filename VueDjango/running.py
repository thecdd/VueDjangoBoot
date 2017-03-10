from apscheduler.schedulers.blocking import BlockingScheduler


# node_modules\.bin\webpack --config webpack.config.js --watch

if __name__ == '__main__':
    executor = BlockingScheduler()
    executor.start()
