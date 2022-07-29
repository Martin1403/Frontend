Frontend 
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
+ ###### [Omnifood](https://github.com/Martin1403/Frontend/tree/master/webpages/omnifood) is fully responsive [webpage](http://localhost:5001/) using grid & flexbox (HTML, CSS, JS)
+ ###### [Natours](https://github.com/Martin1403/Frontend/tree/master/webpages/natours) is [webpage](http://localhost:5002/) using float-layout (HTML, SCSS) - Testing layout
+ ###### [Trillo](https://github.com/Martin1403/Frontend/tree/master/webpages/trillo) is [webapp](http://localhost:5003/) using flexbox-layout (HTML, SCSS) - Testing layout
+ ###### [Nexter](https://github.com/Martin1403/Frontend/tree/master/webpages/nexter) is [webpage](http://localhost:5004/) using grid-layout (HTML, SCSS) - Testing layout
+ ###### [SysAi](https://github.com/Martin1403/Frontend/tree/master/webpages/sysai) is [webpage](http://localhost:5005/) using grid & flexbox (HTML, SCSS, JS) ... Unfinished!!!
