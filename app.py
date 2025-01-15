from pk_pushups_logger_final import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)