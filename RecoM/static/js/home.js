function search(films)
{
    //Search string
    var i,x;
    x = document.getElementById("searchBox").value;
    document.getElementById("searchResult").innerHTML="";
    
    var count=0;

    if(x.length>2)
    {
    
        for(i=0;i<films.length;i++)
        {
            if(films[i].substr(0, x.length).toUpperCase() == x.toUpperCase())
            {
                var anchor = document.createElement("a");
                anchor.href = "/result/" + films[i];
                var textnode = document.createTextNode(films[i].toUpperCase());
                anchor.appendChild(textnode);
                var node = document.createElement("Button");              
                var image = document.createElement("img");
                image.src = "/static/images/movie.jpg";
                node.appendChild(image);
                node.appendChild(anchor);                              
                document.getElementById("searchResult").appendChild(node);
                count++;     
                if(count==10)
                {
                    break;
                }
                console.log(count);
            }
            else
            {
                console.log('Not found');
            }
        }
    }

    
}