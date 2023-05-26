<h1>Habr's articles parser</h1>
  <p>A script for a quick download to file articles from Habr in format: "article title, article URL". You need to choose the articles category from the site and place it to variable "category". For full download i used a list of proxy ip. 
  </p>
<h2>Tools</h2>
  <p>
    <ul>
      <li>Python 3.10</li>
      <li>asyncio</li>
      <li>aiohttp</li>
      <li>Beautiful Soup</li>
      <li>lxml</li>      
    </ul>
  </p>
<h2>Start</h2>
  <p>
    <ul>
      <li>Download the code</li>
      <li>Install requirements <code>pip install -r requirements.txt</code></li>
      <li>You need to use some proxy IPs for full download</li>
      <li>Choose the category name from <code>https://habr.cum/hub/</code></li>
      <li>Put the chosen category to variable <code>category="your_category"</code></li>
      <li>Start script</li>  
    </ul>
  </p>
<hr>
<p>This code was written for educational purposes to learn asyncio and aiohttp.<br>
  
