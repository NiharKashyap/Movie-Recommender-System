function search(films)
{
    //Search string
    var i,x;
    x = document.getElementById("searchBox").value;
    document.getElementById("searchResult").innerHTML="";

    if(x.length>2)
    {
        for(i=0;i<films.length;i++)
    {
        if(films[i].substr(0, x.length).toUpperCase() == x.toUpperCase())
        {
            var anchor = document.createElement("a");
            anchor.href = "/result/" + films[i];
            var textnode = document.createTextNode(films[i]);
            anchor.appendChild(textnode);
            var node = document.createElement("Button");                 // Create a <li> node
            //var textnode = document.createTextNode(films[i]);         // Create a text node
            //node.appendChild(textnode);
            node.appendChild(anchor);                              // Append the text to <li>
            document.getElementById("searchResult").appendChild(node);     // Append <li> to <ul> with id="myList"
            console.log('found');
        }
        else
        {
            console.log('Not found');
        }
    }
    }

    
}