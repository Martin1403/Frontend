Frontend ![](logo1.png) ![](logo3.png)  ![](logo2.png) 
========
![](logo.png)
### Run:
```
git clone https://github.com/Martin1403/Frontend.git && \
cd Frontend && \
docker-compose up --build && \
docker-compose down && \
docker rmi $(docker images --format="{{.ID}}" frontend_*) --force && \
docker volume prune
```

**Example web pages, simple run command and check in the browser. Ctrl+C to exit.**
+ ###### [Chairs](https://github.com/Martin1403/Frontend/tree/master/webpages/chairs) is simple [webpage](http://localhost:5000/) (HTML, CSS)
+ ###### [Omnifood](https://github.com/Martin1403/Frontend/tree/master/webpages/omnifood) is responsive [webpage](http://localhost:5001/) (HTML, CSS)
+ ###### [Natours](https://github.com/Martin1403/Frontend/tree/master/webpages/natours) is [webpage](http://localhost:5001/) using float Layout (HTML, CSS)
+ 