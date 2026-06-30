python3 src/main.py

if [ $? -ne 0 ]; then
    echo "An error occured running src/main.py"
    exit 1
fi

cd public && python3 -m http.server 8888