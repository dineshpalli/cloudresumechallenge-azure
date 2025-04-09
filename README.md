# Cloud Resume Challenge with Microsoft Azure: My Journey, Struggles, and Insights

![image](https://raw.githubusercontent.com/dineshpalli/cloudresumechallenge-azure/refs/heads/main/DineshPalli_CRC.png?token=GHSAT0AAAAAADBDGPQ5NFVXTZL4HSMEXJACZ7W3PBQ)

 *Architecture of the Cloud Resume Challenge on Azure. The static resume site is hosted on Azure Storage and exposed to the web via a content delivery network service (Azure Front Door or CDN) for global, secure access. An Azure Function app provides a Python API for the visitor counter, with data persisted in an Azure Cosmos DB database. All components (storage, function, database, networking) are defined as code and deployed through CI/CD pipelines.*

## Introduction

Standing at the foot of the **Cloud Resume Challenge**, I felt a mix of excitement and dread. I was comfortable discussing cloud concepts in theory, yet I had no real project to show for it. This gap between knowledge and experience was gnawing at me. It echoed the ancient Greek proverb *pathemata mathemata* – meaning *“learning through suffering/experience.”* In other words, the best way to learn is by doing, even if it means struggling. Embracing that wisdom, I decided to conquer my doubts and take action. What followed was a challenging yet exhilarating journey through a 16-step cloud project that would test my technical skills, resilience, and problem-solving like never before.

Thanks to @Jan F. Lammering and the amazing HR team of @Oraylis (@[Sonja Kühle-BogenschneiderView Sonja Kühle-Bogenschneider’s profile ](https://www.linkedin.com/in/sonja-kühle-bogenschneider?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAADW0X70Bm2e6d3Kh0e6v259VCoHrt0eV9fg), @[Anne Müller-KemlerView Anne Müller-Kemler’s profile ](https://www.linkedin.com/in/anne-müller-kemler-a43962222?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAADgGxVMBxlTsrRgVW9Y_rMSegDG4Gr6_l1I), @[Georgia ThumeView Georgia Thume’s profile](https://www.linkedin.com/in/georgia-thume-883a59ab?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABd4fqMBR9JQR9rbliGxa4j16Qw0n1OhBe0), , for inspiring me to expound my knowledge and skills with Azure and the related technologies.

Related Links:

My website - https://www.dineshpalli.com, please leave your valuable feedback in the comments section below.

GitHub Repo (Feel free to clone, would be amazing if you could tag me) - https://github.com/dineshpalli/cloudresumechallenge-azure



## What is the Cloud Resume Challenge?

The **Cloud Resume Challenge** is a rigorous multi-step project originally created by cloud architect [Forrest Brazeal](https://www.linkedin.com/in/forrestbrazeal/). It’s designed as a bridge between attaining cloud certifications and landing a cloud job, helping you go from “certified to hired” in a practical way ([The Cloud Resume Challenge](https://cloudresumechallenge.dev/)). The challenge consists of 16 steps (yes, **16!**) that cover both front-end and back-end development, cloud services, infrastructure as code, CI/CD, and more. Forrest deliberately doesn’t hand-hold participants through these steps – the expectation is that you figure things out yourself and learn through the struggle ([Cloud Resume Challenge by Forrest Brazeal](https://heyvitech.hashnode.dev/cloud-resume-challenge-by-forrest-brazeal#:~:text=You%20will%20not%20be%20guided,the%20best%20method%20to%20learn)). This trial-by-fire approach is intentional because solving problems on your own is one of the best ways to gain meaningful cloud engineering experience. In fact, many people with years of IT experience have taken on this challenge to sharpen their skills ([Cloud Resume Challenge by Forrest Brazeal](https://heyvitech.hashnode.dev/cloud-resume-challenge-by-forrest-brazeal#:~:text=Fun%20fact%20,Challenge%20is%20worth%20a%20try)), which speaks to its value and difficulty.

Here’s a quick rundown of the **16 steps** in the Azure edition of the Cloud Resume Challenge:

1. **Certification:** Start by earning a foundational Azure cert (I have not yet acquired an azure certification).
2. **HTML:** Write your resume in HTML.
3. **CSS:** Style the resume with CSS to make it presentable.
4. **Static Website:** Host your resume as a static website (in Azure, that means using an Azure Storage account’s static website feature).
5. **HTTPS:** Implement HTTPS for your site (e.g. via Azure Front Door or CDN to get SSL).
6. **DNS:** Set up a custom domain name for your website.
7. **JavaScript:** Add interactivity – in this case, a JavaScript snippet to fetch and display a visitor counter.
8. **Database:** Create a database to store the visitor count (Azure Cosmos DB in the Azure challenge).
9. **API:** Develop an API endpoint that the JavaScript can call to get/update the count (using Azure Functions).
10. **Python:** Write the API code in Python (the Azure Function’s runtime).
11. **Tests:** Write tests for your code (unit tests for the Python function, and maybe simple frontend tests).
12. **Infrastructure as Code:** Define your infrastructure in code (using a tool like Terraform or Azure Bicep) instead of clicking in the portal.
13. **Source Control:** Use source control (GitHub) to manage your code and IaC scripts.
14. **CI/CD (Back End):** Set up a CI/CD pipeline to automate deployment of your back-end (the Azure Function and related infrastructure).
15. **CI/CD (Front End):** Set up a CI/CD pipeline to automate deployment of your front-end (the static website).
16. **Blog Post:** Write a blog (or LinkedIn article!) about your journey and lessons learned.

As you can see, the challenge is an **end-to-end project** touching almost every aspect of cloud and web development: front-end design, back-end APIs, databases, networking, authentication, automation, and more. It’s intense. No tutorials, no courses, just dragging myself through dirt? So, I finished cloud resume challenge in MS Azure - the turnkey github repo can be found here - feel free to fork / clone / star the repo. I knew I would hit roadblocks in each of these areas – and indeed I did. But with each obstacle came an opportunity to learn and grow. There were severael moments across the challenge where i had to show myself that I am with it or on it, which helped me learn a lot and not give up at the slightest sight of challenge / discomfort. This made me imbue a lot of learning and experience like, figure out where something broke, what broke, why it broke and then devising plans to how to fix the broken things, doing 'smoke-tests' and fixtures.

Forrest Brazeal, the challenge's creator, acknowledges that it will require:

- **Multiple long evenings** of work
- **Extensive research**
- **Significant self-learning**

I spent the the long hours of work at the end of November, December and beginning of January, doing step 2 and gaining the third. In the next sections, I’ll walk through the major challenges I faced in each step of CRC and what I learned from overcoming them.

## The Challenges Faced and Lessons Learned

### 1. Domain Name Registration & Setup

**Challenge:** One of the first tasks was to get a custom domain for my resume website. This seemingly simple step turned into a quest of its own. Which domain registrar to choose? How to ensure DNS would be reliable? I was new to buying domains and worried about getting scammed or stuck with poor service. After some research and community recommendations, I chose **Porkbun** as my registrar. Why Porkbun? Two big reasons stood out: (1) **Transparent, affordable pricing** – they show first-year and renewal prices clearly with no hidden fees, so I knew exactly what I’d pay ([Does anyone here have a domain at Porkbun? Is it worth buying there, or will I get tricked like I did with Namecheap? T.T : r/webdev](https://www.reddit.com/r/webdev/comments/1gp10fd/does_anyone_here_have_a_domain_at_porkbun_is_it/#:~:text=1.%20Transparent%20pricing%20,year%20and%20renewal%20prices%20upfront)). (2) **Robust DNS management** – Porkbun’s interface for DNS records is very user-friendly and powerful, which is crucial when configuring custom records for Azure ([Does anyone here have a domain at Porkbun? Is it worth buying there, or will I get tricked like I did with Namecheap? T.T : r/webdev](https://www.reddit.com/r/webdev/comments/1gp10fd/does_anyone_here_have_a_domain_at_porkbun_is_it/#:~:text=1.%20Transparent%20pricing%20,year%20and%20renewal%20prices%20upfront)). Additionally, Porkbun provides free WHOIS privacy and had great reviews for reliability. 

Purchasing the domain was the easy part. The real struggle came when hooking it up to my Azure resources. I had to create DNS records that point my new domain to the Azure static site (via [Azure Front Door](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview) (Formerly CDN)). This involved adding **CNAME records** for the subdomain (www) and an **A record** or alias for the root/apex domain. Initially, I wasn’t sure which records were needed – should I use an A record pointing to an IP? Or a CNAME to some azure domain? I learned that Azure Front Door provides a **profile URL** (like `yourfrontdoor.azurefd.net`) which you map via a CNAME. For the root domain, I ended up using an ALIAS or ANAME record (since CNAME at root isn’t allowed by DNS standards). It took some trial and error, and DNS changes take time to propagate, so I spent quite a few anxious hours waiting to see if my site would resolve on my domain. Seeing **“DNS_PROBE_FINISHED_NXDOMAIN”** errors during that wait was nerve-wracking! Eventually, the DNS setup clicked, and my domain began pointing to my Azure front end. 

**Lesson learned:** Choosing a good registrar makes life easier, but you still need patience (DNS changes can take hours). I also got a crash course in DNS record types and discovered the importance of documentation – Porkbun’s and Azure’s docs became bedtime reading. Most importantly, I overcame the fear of “breaking something” with DNS. Now, managing domains feels much less enigmatic.

### 2. Understanding DNS

**Challenge:** While setting up the domain, I realized I had a **knowledge gap in DNS (Domain Name System)** itself. I knew the concept in abstract – DNS translates domain names to IP addresses – but I’d never configured DNS settings manually for a custom domain. Why did I need a CNAME vs an A record? What’s TTL? I decided to pause and educate myself on DNS fundamentals so I wouldn’t be just guessing. 

I learned that **DNS is essentially the phonebook of the Internet** – it maps human-friendly names (like `myresume.com`) to the numeric IP addresses that computers use ([What is DNS? | How DNS works | Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/#:~:text=What%20is%20DNS%3F)). When someone types my domain, a DNS query is made behind the scenes to find the matching IP or address for the server where my site is hosted. I also learned about **authoritative name servers** (which hold the DNS records for my domain) and **recursive resolvers** (the “DNS librarians” that fetch the answer) ([video](https://www.youtube.com/watch?v=mpQZVYPuDGU, [What is DNS? | How DNS works | Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/#:~:text=There%20are%204%20DNS%20servers,involved%20in%20loading%20a%20webpage)), [What is DNS? | How DNS works | Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/#:~:text=it%20serves%20as%20a%20reference,to%20the%20requested%20record%2C%20it)). This helped me appreciate why sometimes I’d get different results during propagation – DNS servers around the world take time to update.

In practice, for my resume site I set up the following DNS records:
- `A record` for `myresume.com` -> Points to Azure Front Door’s anycast IP (provided by Azure when verifying the domain).
- `CNAME record` for `www.myresume.com` -> Points to the Front Door hostname (e.g., `myresume.azurefd.net`).

Understanding these settings was empowering. Instead of blindly following a tutorial, I knew *why* these records were needed. I even troubleshot a mistake where I’d misconfigured the CNAME – browsers were showing a security certificate error because the domain wasn’t properly recognized by Front Door. Fixing that required me to **verify the custom domain** within Azure Front Door (by adding a specific verification ID as a TXT record). It was a lot of back-and-forth, but eventually I got the DNS configuration stable.

**Lesson learned:** **DNS is crucial** in any cloud project with custom domains, and you can’t treat it as a black box. By investing time in learning how DNS works (the hierarchy, record types, propagation), I became much more confident in setting up and troubleshooting domain issues. This foundational knowledge paid off later when I had to diagnose why *HTTPS wasn’t working* (spoiler: it was a DNS misconfiguration on my part!). The key takeaway: when in doubt, go back to fundamentals – understanding the basics will illuminate the path forward.

### 3. Azure Subscription & Resource Management

**Challenge:** Next up was working in the **Azure cloud** environment itself – creating resources and managing them. I signed up for an Azure account (I already had one from my certification prep) and created a dedicated **Resource Group** to contain everything for this project. Even with some Azure knowledge, I felt overwhelmed when I started enumerating all the services I needed: a Storage Account for the static site, a Cosmos DB instance, an Azure Function app, an Azure Front Door profile for CDN/HTTPS, etc. The Azure Portal has *so many* options that it’s easy to feel lost. I was also conscious that some services might incur costs. I had to plan carefully to stay within free tiers (Azure Cosmos DB has a free tier of 400 RU/s, Azure Functions consumption plan is essentially pay-per-use, and Azure Front Door has a minimal cost for low traffic). 

Setting up **Azure Storage Static Website** was straightforward: you enable “Static website” on a Storage Account and upload your HTML/CSS files to the special `$web` container. But enabling **HTTPS** on a custom domain was not straightforward. Azure Storage static sites don’t natively support custom domain HTTPS, so Azure’s documentation recommends putting a CDN or Front Door in front ([certificate - Enabling HTTPS for a Azure blob static website - Stack Overflow](https://stackoverflow.com/questions/61662502/enabling-https-for-a-azure-blob-static-website#:~:text=From%20this%20link%3A)). I opted for **Azure Front Door** (Classic) because it provides a managed SSL certificate for custom domains and also offers global caching and routing features. Azure Front Door required me to **add my custom domain** to its frontend hosts, which in turn required the DNS mapping we discussed earlier. I stumbled here with validation – Front Door wouldn’t accept my domain until I created a **TXT record** it provided for verification. It felt like a chicken-and-egg at first: to add domain in Front Door I need DNS, and for DNS to work I need Front Door’s endpoint. The solution was to follow Azure’s sequence precisely: verify domain ownership via TXT record, add the domain to Front Door, then update the CNAME/A records. Once done, Front Door provisioned an SSL cert for my domain automatically ([certificate - Enabling HTTPS for a Azure blob static website - Stack Overflow](https://stackoverflow.com/questions/61662502/enabling-https-for-a-azure-blob-static-website#:~:text=1)) (a process that took ~20 minutes). Seeing the green lock icon next to my URL was a moment of triumph.

Managing **Azure resources** also taught me about keeping things organized. I named resources with a consistent prefix, set tags for project name, and noted down in a README what each resource was for. At one point, I hit a snag where deployments were failing because I reached the limit of one free Front Door (the classic SKU allowed only one using free tier). I had to delete and recreate Front Door to tweak settings, which was a pain to do manually (this foreshadowed the need for Infrastructure as Code, which I implemented later). I also nearly forgot to turn on the **“Always On” setting for my Azure Function** (to prevent cold start latency), but caught it during testing.

**Lesson learned:** **Planning and resource management** in Azure is critical. Before jumping in, outline the architecture and identify the Azure services you’ll use. This helps in creating resources in a logical order and avoiding surprises (like service limits or prerequisite dependencies). I learned to navigate the Azure Portal more efficiently, but also realized the value of automation – clicking around is fine for initial exploration, but IaC would save me from repetitive manual setup when I inevitably had to rebuild or modify resources. Additionally, I gained experience with Azure Front Door and how it integrates with other services (DNS, Storage), which is a valuable skill on its own. 

### 4. Frontend Development (HTML, CSS, Dark Mode)

**Challenge:** Concurrently with the cloud setup, I had to build the **frontend of my resume website**. This involved writing the resume content in HTML, styling it with CSS, and making it functional and nice-looking. I’m not a front-end developer by trade, so initially I had imposter syndrome: “Is my HTML/CSS good enough? Does it look professional?” My first version of the site was very basic – just text on a white background. It worked, but it didn’t *wow*. I struggled with CSS to create a pleasant design. Rather than reinvent the wheel, I found a simple open-source HTML/CSS template as a starting point and tailored it to my needs (changed the color scheme, fonts, and layout to match my style). This saved me a ton of time and frankly resulted in a better-looking site.

One fun addition I decided on was **Dark Mode**. Many modern websites offer a dark theme, and I wanted to show that I pay attention to UX details. I implemented this using CSS media queries for the `prefers-color-scheme`, as well as a JavaScript toggle button. This was a small rabbit hole of its own – ensuring that icons and images looked good on both dark and light backgrounds, and that my text remained readable. After a bit of tweaking, I got a nicely togglable dark mode working purely with CSS classes and a few lines of JavaScript to remember the user’s preference.

Another challenge was making the site **responsive**. I ensured the layout used relative units and flexbox, so it would display properly on mobile phones, tablets, etc. Testing on my own phone revealed some font sizes were too large and a section of text was overflowing the screen. I adjusted the CSS and learned how to use responsive meta tags and viewports properly.

While working on the frontend, I also embedded the code for the **visitor counter display**. At this point, I hadn’t built the back-end yet, but I knew I’d be calling an API to get a visitor count. So I wrote a small `<span id="visitors">` in the HTML and a `<script>` that would later fetch from an endpoint (I used a dummy number or simple counter logic temporarily to see it in action). This helped connect the dots between front-end and back-end early on.

**Lesson learned:** From a front-end perspective, I learned to balance **technical depth with visual appeal**. This challenge wasn’t just about cloud services; it was also about presenting *my resume*, essentially marketing myself. So the site needed to be polished. I gained confidence in HTML/CSS, learning a few new tricks (like how to do dark mode, and the power of a good CSS reset). I also learned not to be afraid to use templates or libraries – leveraging existing designs is perfectly fine as long as you customize and understand them. In a way, this mirrors real-world development: you don’t always start from scratch, but you **do** need to know how to adapt components to your needs.

### 5. Backend Development (Azure Functions, Cosmos DB, Python API)

**Challenge:** Now for the **back-end** – the engine behind my visitor counter. The requirements were to have a database that stores a visitor count and an API that the front-end can call to increment and retrieve this count. In the AWS version of the challenge, people use DynamoDB and Lambda; for Azure, the equivalents are **Azure Cosmos DB** and **Azure Functions**. I chose Cosmos DB with the Core (SQL) API, in serverless mode (The **serverless mode**, is ideal for small-scale applications like the Cloud Resume Challenge. In serverless mode, I only pay for the request units (RUs) consumed by my database operations, making it highly cost-effective for low-traffic.) to keep things JSON/document-based. Cosmos is a powerful, globally distributed NoSQL database, but it was also new territory for me.

Why Not Other Cosmos DB APIs?

While Azure Cosmos DB supports multiple APIs (e.g., MongoDB, Cassandra, Gremlin), the **NoSQL API** is the most native and optimized for Cosmos DB. The other APIs are useful if I am migrating an existing application or need specific features (e.g., graph data for Gremlin), but they add unnecessary complexity for the Cloud Resume Challenge.

One immediate concept I had to learn was the **Partition Key** in Cosmos DB. When creating a container (table), Cosmos asks for a partition key path. Initially, I was puzzled – for a simple visitor counter, did I even need multiple partitions? After reading, I learned that every item in Cosmos *must* have a partition key; it’s how Cosmos scales and distributes data. It’s best to choose a partition key that will evenly distribute data and be used in queries ([Stack Overflow](https://stackoverflow.com/questions/45067692/azure-cosmos-db-understanding-partition-key), [Documentation by Microsoft](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview#choose-a-partition-key)). In my case, since I only had one item (a counter), it didn’t matter much – I could use something like `/id` or `/siteName` as the partition key just to satisfy the requirement. I ended up using a constant partition key value for the single counter record. This was admittedly not a perfectly scalable design (if this were a high-traffic multi-counter scenario, a single partition could be a hotspot), but it was sufficient for the project scope.

What is Azure Synapse Link?

Azure Synapse Link enables near real-time analytics on operational data stored in Azure Cosmos DB without requiring an Extract, Transform, and Load (ETL) process. It essentially acts as a **bridge**between operational (OLTP) and analytical (OLAP) systems, allowing data to be accessed efficiently for analytics workloads.

Next, I tackled the **Azure Function**. I wrote a Python Azure Function with an HTTP trigger. This function’s job was simple in description: when hit with a GET or POST request, connect to Cosmos DB, increment a counter, and return the updated count as JSON. I discovered Azure Functions has a feature called **output binding** for Cosmos DB – which means I could configure the function to automatically write to a Cosmos DB item without writing all the boilerplate CRUD code. However, to better understand the process (and since output binding required some specific data shaping), I chose to manually use the [Azure Cosmos DB Python SDK](https://learn.microsoft.com/en-us/azure/developer/python/sdk/azure-sdk-overview) inside the function.

```python
import sys
import json
import azure.functions as func
import logging
import os
from azure.cosmos import CosmosClient, PartitionKey

# Initialize Azure Function with function-level authentication
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


def _get_cosmos_container():
    """
    Lazily load Cosmos DB connection details and client.
    This function checks environment variables at runtime
    (rather than at module import time).
    """
    required_env_vars = [
        "COSMOS_DB_ACCOUNT_URI",
        "COSMOS_DB_ACCOUNT_KEY",
        "COSMOS_DB_NAME",
        "COSMOS_DB_CONTAINER",
    ]

    # Check for any missing environment variables.
    missing_vars = [var for var in required_env_vars if var not in os.environ]
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )

    # Extract Cosmos DB connection details from environment variables.
    cosmos_db_uri = os.environ["COSMOS_DB_ACCOUNT_URI"]
    cosmos_db_key = os.environ["COSMOS_DB_ACCOUNT_KEY"]
    cosmos_db_name = os.environ["COSMOS_DB_NAME"]
    cosmos_db_container = os.environ["COSMOS_DB_CONTAINER"]

    # Set up the Cosmos DB client and container.
    client = CosmosClient(cosmos_db_uri, credential=cosmos_db_key)
    database = client.get_database_client(cosmos_db_name)
    container = database.get_container_client(cosmos_db_container)

    return container


# HTTP trigger function that increments and returns the visitor count
@app.route(route="http_trigger_py")
def get_visitor_count(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing getVisitorCount request. Kindly wait...")

    try:
        # Initialize Cosmos container on-demand (includes env var checks)
        container = _get_cosmos_container()

        # Try to fetch the existing count document with id="1"
        item = None
        try:
            item = container.read_item(item="1", partition_key="1")
            logging.debug(f"Found item: {item}, the existing count document.")
        except Exception as e:
            # If document doesn't exist, initialize with count=42
            # 42 is used as a fun reference to "Hitchhiker's Guide to the Galaxy"
            logging.error(f"The count document not found or an error occurred: {e}")
            item = {"id": "1", "count": 42}

        # Get current count, defaulting to 42 if not found
        current_count = item.get("count", 42)

        # Ensure count is a valid integer; if corrupted, reset to 42
        if not isinstance(current_count, int):
            logging.error(
                f"Current count is invalid. Resetting to 42! "
                f"(Why 42 you ask? It's a galactic inside joke. "
                f"Grab a towel and go figure it out). Item: {item}"
            )
            current_count = 42

        # Increment the visitor count
        new_count = current_count + 1
        item["count"] = new_count

        # Save updated count back to Cosmos DB
        container.upsert_item(item)
        logging.info(f"Updated visitor count to {new_count}")

        # Return new count as JSON response
        response_body = {"count": new_count}
        return func.HttpResponse(
            body=json.dumps(response_body),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        # Handle any unexpected errors
        logging.error(f"Error updating visitor count: {e}", exc_info=True)
        error_body = {"error": "Unable to retrieve and update visitor count."}
        return func.HttpResponse(
            body=json.dumps(error_body),
            status_code=500,
            mimetype="application/json",
        )
```

Writing the Python code was straightforward logic-wise, but I ran into environment issues. Azure Functions for Python uses specific package versions and a structure (`requirements.txt`, etc.). I had to ensure the Cosmos DB Python SDK (`azure-cosmos`) was added to my `requirements.txt` so that it would be available in Azure. Locally, I tested the function using Azure Functions Core Tools – a local emulator. This helped a lot: I could fire requests at `http://localhost:7071/api/visitors` and see if it updated the count.

For the database operations, I used the **“upsert”** functionality. Upsert is a combined *insert or update* operation – if the item (document) doesn’t exist, it creates it; if it does exist, it updates it ([Source](https://www.cockroachlabs.com/blog/sql-upsert/)). This was perfect for a visitor counter: every time the API is called, upsert an item with key “counter” and increment a field. If it’s the first visitor ever, the item gets created with count=1; otherwise, it just updates the existing count. Using upsert saved me from writing separate logic for create vs update.

One tricky part was ensuring my function had permission to access the Cosmos DB. In Azure, my function and Cosmos were in the same resource group, but I still needed to provide the Cosmos DB connection string to the function (as an environment setting) or set up a managed identity. For simplicity, I stored the Cosmos DB keys in an Azure Functions application setting (which I later moved to a secure place when using IaC). In a production scenario, I might use a managed identity so the function can fetch secrets from Azure Key Vault, but I kept things straightforward for now.

**Lesson learned:** Building the back-end solidified my understanding of **serverless functions and database operations in the cloud**. I learned how to interact with Cosmos DB in Python and the concept of upsert operations. More importantly, I experienced first-hand the stateless nature of serverless: the function could be invoked multiple times in parallel, so I had to consider concurrency on the counter (Cosmos DB’s etag concurrency control could be relevant if this was high-scale). For this project, Cosmos’s built-in “last write wins” with upsert sufficed. I also became comfortable with Azure Functions tooling – creating the function, running it locally, deploying it (more on deployment in CI/CD section), and monitoring it. When I deployed the function to Azure for the first time and called the API endpoint from my website, seeing the number increment on my page felt like magic! It was a full-stack accomplishment – from browser to cloud and back.

### 6. Backend and Frontend Integration with Javascript

During the same, I learnt what CORS (Cross Origin Resource Sharing) is. CORS is a mechanism that relaxes the SOP (What is SOP? Answered in the following paragraph). It allows web applications on one origin to request resources from servers on a different origin *if the server permits it*.

Mechanism:

- Web browsers send special HTTP headers (such as `Origin`, `Access-Control-Request-Method`, etc.) when making a cross-origin request.
- The server can respond with corresponding headers (like `Access-Control-Allow-Origin`, `Access-Control-Allow-Credentials`, etc.) to either grant or deny permission.
- If the server grants permission, the browser allows the cross-origin request to succeed.

Definition: SOP is a fundamental security restriction enforced by web browsers. It states that a web page (i.e., script) can only access resources (like data or the DOM) from the *same origin*—where an origin is defined by the combination of scheme (protocol), host (domain), and port.

Purpose: It prevents malicious scripts on one page from obtaining sensitive data from another page on a different domain. Essentially, it *blocks cross-domain reads* unless explicitly allowed.

The relationship between SOP and CORS is that

- **SOP** is the default browser security model that **blocks cross-origin resource access**.
- **CORS** is a standardized way for a server to **opt-in** to allowing cross-origin requests despite SOP. Without CORS (or other bypass mechanisms like JSONP in older contexts), the browser would block most cross-origin calls to protect users from potential security risks.

In short, **CORS** exists as a controlled mechanism to **override** or **relax** the **same-origin policy** under specific, secure conditions configured by the server.

I learnt what DOM - Document Object Module is.

**DOM** stands for **Document Object Model**, which is a programming interface (API) for HTML and XML documents. It provides a structured, hierarchical representation of the document, allowing scripts (such as JavaScript) to:

1. **Access** the elements in the document (like `<div>`, `<p>`, `<img>`, etc.),
2. **Modify** their content and attributes,
3. **Add or remove** elements,
4. **Respond to events** (e.g., clicks, keyboard input).

When a web page is loaded, the browser parses the HTML (and possibly XML) and constructs a **tree-like** model of the document, where each node represents a part of the page (an element, a text node, an attribute, etc.). This tree of nodes is what we call the DOM. Because the DOM is an interface, languages like JavaScript can manipulate it in real time, enabling dynamic, interactive web pages.

I used DOM to define what clicking some buttons does - for example changing the language from English to German and vice-versa, and dark / light toggle and a not-so-hidden confetti blast.

### 7. CI/CD Implementation (GitHub Actions Pipelines)

**Challenge:** With front-end and back-end built, I needed to set up **Continuous Integration/Continuous Deployment (CI/CD)** so that any changes I push to my code repository would automatically build and deploy the latest version of my resume site. This is a crucial part of the challenge – it demonstrates ability to automate and streamline operations, which is highly valued by employers. I chose **GitHub Actions** for CI/CD, as it’s natively integrated with GitHub where my code resides.

#### Deploying the function (before the CI / CD)

Next comes KUDU, in the azure function app context. **Kudu** is the deployment engine and a set of related tools that run behind the scenes in Microsoft Azure App Service like function apps, web apps. Features of Kudu include:

1. **Deployment Automation**:
   - Kudu handles the deployment process for Function App, whether we are deploying from:
     - Git repositories
     - GitHub
     - Azure DevOps
     - Local ZIP files
   - It automatically builds and deploys our code to the Function App.
2. **Source Control Integration**:
   - Kudu integrates with Git and other source control systems to enable continuous deployment.
   - When we push changes to our repositories, Kudu automatically pulls the latest code and deploys it to our Function App.
3. **Diagnostic Tools**:
   - Kudu provides a **diagnostic console** where qw can run commands, inspect logs, and troubleshoot issues.
   - We can access logs for:
     - Application logs
     - Deployment logs
     - Web server logs
4. **File System Access**:
   - Kudu gives us access to the file system of Function App.
   - We can browse, upload, download, and edit files directly through the Kudu interface.
5. **Environment Management**:
   - Kudu provides detailed information about the runtime environment of our Function App, including:
     - Environment variables
     - Installed software
     - System settings
6. **WebJobs and Background Tasks**:
   - Kudu supports the management of **WebJobs**, which are similar to Azure Functions but run in the context of an App Service plan.

I deployed my function app, as a zip file from local Azure CLI on VS Code. After deploying, it did not work perfectly, as the script that points to function app python script was absent. And a small tip, to have all the environmental variables,

APPLICATIONINSIGHTS_CONNECTION_STRING, AzureWebJobsFeatureFlags, AzureWebJobsStorage, COSMOS_DB_ACCOUNT_KEY, COSMOS_DB_ACCOUNT_URI, COSMOS_DB_CONTAINER, COSMOS_DB_NAME, ENABLE_ORYX_BUILD, FUNCTIONS_EXTENSION_VERSION, FUNCTIONS_WORKER_RUNTIME, SCM_DO_BUILD_DURING_DEPLOYMENT, WEBSITE_CONTENTAZUREFILECONNECTIONSTRING, WEBSITE_CONTENTSHARE. Then I had to create an __init__.py file in the directory. Moreover I had to deploy only the root folder of the app and not th entire github repo, which means that I deploy only the backend/api folder as my function app. This is because Azure functions are folder based and and should contain function.json that points to the function app script, and tells azure how to build and trigger the function. Deploying the whole repo confuses Azure as it looks for function.json script in the root directory of the deployed zip / package. Then it worked. After that I got the function url and copied the default key.

#### CI / CD

Setting up GitHub Actions for Azure required creating a **Service Principal** – essentially a special Azure AD identity with permissions that GitHub Actions can use to deploy resources on my behalf. A service principal is an identity made for automated tools (like CI/CD pipelines) rather than a human user ([Service principals for CI/CD - Azure Databricks | Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/ci-cd/ci-cd-sp#:~:text=This%20article%20describes%20how%20to,automated%20tools%20and%20applications%2C%20including)). I created one using Azure CLI (`az ad sp create-for-rbac` command), giving it contributor access to my resource group. This generated an app ID, tenant ID, and client secret – which I stored as secrets in my GitHub repository. It felt a bit like giving keys to a robot: with those credentials, my GitHub Actions could log in to Azure and perform deployments securely.

I ended up creating **two workflows**: one for the front-end (resume website) and one for the back-end (function + infrastructure). The front-end workflow was triggered on pushes to the `frontend` folder (where my HTML/CSS/JS live). It would build any assets (in my case, just zipping files) and then use Azure CLI to upload files to the Azure Storage `$web` container (overwriting the old files). I also used an Azure CLI command to **purge the Front Door cache** for my site, so that the new changes would reflect immediately globally.

The back-end workflow was a bit more involved. It was triggered on pushes to the `backend` or `infra` (Terraform) code. Its steps were:
- Checkout code and set up Python environment.
- Run tests (more on tests in next section).
- Package the Python Azure Function (basically `func azure functionapp publish` or deploying via zip).
- Deploy the Azure Function code to Azure. For this I used the official Azure Functions Action or used Azure CLI to zip deploy to the function app.
- Run Terraform to apply any infrastructure changes (this included creating or updating the Cosmos DB, Function App itself, etc., if I changed IaC definitions).

One major struggle here was **configuring Terraform in CI**. I had to store the Terraform state somewhere. I chose to use Azure storage as a remote backend for Terraform state, which required setting up a storage account and container for state files. Getting all these pieces to work in GitHub Actions YAML took many trial runs. My initial pipeline runs failed because of missing permissions – the service principal needed additional rights (e.g., to create new resources defined in Terraform). I iteratively adjusted the IAM roles in Azure and the scope until the pipeline could execute without errors.

Another issue was secrets management. I had to pass sensitive information (like the Cosmos DB connection string, or the Azure Function’s settings) into the workflow. I leveraged GitHub Secrets and masked variables, and for Azure Function settings, I ended up storing them in Azure and using the workflow to update them if needed (for instance, Terraform can set app settings as part of the Function App resource definition).

There was a moment when my CI pipeline kept failing on the Terraform step, and I was stuck past midnight combing through error logs. The error was about a dependency conflict that didn’t make sense. After a frustrating hour, I realized it was due to me using an outdated Terraform Azure provider version. I updated it and things magically worked. This taught me to pay attention to the details in error logs and also to ensure I’m using updated tools.

**Lesson learned:** Setting up CI/CD gave me invaluable experience in **automation and DevOps practices**. I learned how to authenticate a GitHub Action runner with Azure securely, how to use the Azure CLI and Azure Actions within a workflow, and how to handle state and secrets. The big win is that now I can push a change (say, tweak my resume text or fix a bug in the Python API) and within minutes the change is live on my website without any manual steps. This is the power of CI/CD – faster iterations and fewer human errors in deployment. I also learned to be patient and systematic when debugging pipeline issues. It’s a different kind of debugging than code debugging, but using a **heuristic approach** (check logs, add echo statements to see variables, upgrade tools, etc.) eventually resolves the issues. By the end, I had a **fully automated deployment process**, which felt like having an extra team member handling ops for me.

Special shout out to GitKraken for providing an exceptional graphical user interface for my repository management. Their intuitive merge conflict resolution tool has significantly streamlined my workflow, making the process of resolving merge conflicts remarkably efficient and user-friendly.

### 8. Infrastructure as Code (Terraform vs Azure Bicep)

**Challenge:** One of the more intimidating steps for me was implementing **Infrastructure as Code (IaC)**. This means writing code to define and provision all the cloud resources (as opposed to clicking in the Azure Portal). The challenge gave the option of using tools like AWS CloudFormation, Azure Resource Manager templates, Azure Bicep, or Terraform. In the Azure world, the two popular IaC choices are **Azure Bicep** (Microsoft’s domain-specific language for ARM templates) and **Terraform** (HashiCorp’s multi-cloud IaC tool). I was torn on which to use. Bicep is tailor-made for Azure and doesn’t require maintaining a separate state file, whereas Terraform has the advantage of being widely used in industry and working across different providers.

After some deliberation, I chose **Terraform**. My reasons were: (1) I wanted to learn a tool I can apply to multiple clouds in the future – Terraform’s provider system lets you manage not just Azure but AWS, GCP, and even third-party services with one language ([Infrastructure as Code on Azure: Bicep vs. Terraform vs. Pulumi - Xebia](https://xebia.com/blog/infrastructure-as-code-on-azure-bicep-vs-terraform-vs-pulumi/#:~:text=Terraform%20is%20an%20open%20source,a%20storage%20account%20using%20Terraform)). (2) Terraform has a large community, and I found more examples/community modules for Azure in Terraform than for Bicep. (3) I was already familiar with basic Terraform from a previous mini-project, so I had a slight comfort advantage. That said, I acknowledge Bicep is fantastic for Azure-only projects and has the benefit of no separate state management (state is handled by Azure). It was a close call.

Implementing Terraform for my project meant writing configuration for each resource: the resource group, storage account (with static website enabled), Cosmos DB account and database/container, the Function App (and its plan), Front Door configuration (Front Door in Terraform was particularly complex due to multiple sub-resources for routes, endpoints, etc.), and even DNS records (Terraform Azure DNS module). This was a **massive learning exercise**. My Terraform config spanned several files for logical separation. I learned how to use Terraform modules and outputs to pass values around (for example, passing the storage account’s primary web endpoint to an output). 

There were moments of head-scratching, like how to get the Cosmos DB keys and feed them into Azure Function settings automatically. I discovered Terraform has the ability to retrieve those via the `azurerm_cosmosdb_account` data source after creation, which I could then use in the Function’s app settings resource block. It felt like wiring up an intricate machine via code.

The biggest benefit came later: when I needed to tweak something in my architecture (like switch to a different SKU for Front Door or add a new environment variable), I simply changed the code and ran `terraform apply`. Terraform figured out the necessary changes (often called the *execution plan*) and applied them in the correct order. This was so much easier than clicking through the portal for each change. Moreover, if I ever needed to recreate the whole environment (say, for testing or if something went wrong), I could do so with one command. It gave me confidence that my setup was reproducible.

**Lesson learned:** Adopting IaC early on in a project is worth the upfront investment. I learned both the syntax and the nuance of Terraform, and also got a taste of the differences between IaC tools. Notably, I learned that **Terraform (being cloud-agnostic)** requires you to configure a provider and manage state, but it offers flexibility to manage any service (in fact, I used it to configure DNS records on Azure as well). In contrast, a tool like Bicep is **Azure-specific but deeply integrated**, which means quicker support for new Azure features ([I was pleasantly surprised | Terraform vs Bicep | by Kaushik - Medium](https://medium.com/@gayal.kaushik/terraform-vs-bicep-honest-feedback-332a54d9ace2#:~:text=Medium%20medium,Also%2C%20terraform%20can)) ([Infrastructure as Code on Azure: Bicep vs. Terraform vs. Pulumi - Xebia](https://xebia.com/blog/infrastructure-as-code-on-azure-bicep-vs-terraform-vs-pulumi/#:~:text=Terraform%20is%20an%20open%20source,a%20storage%20account%20using%20Terraform)). For example, if Azure launches a new service, Bicep can likely use it day one, whereas Terraform might take time for a provider update. These insights into tool choices are valuable for architecture decisions in a professional setting. Ultimately, the Terraform experience strengthened my infrastructure mindset – I treat infrastructure as part of the codebase now, subject to version control and continuous deployment just like application code.

### 9. Testing & Debugging

**Challenge:** With everything built and deployed through pipelines, I had to ensure it all actually *worked* reliably. This meant  **smoke - testing** each part and **debugging** any issues that arose. I wrote a few tests for the Python function using Python’s `unittest` framework (could have used `pytest` as well). For example, I simulated a request to the function and checked that the response contained a count and that the count increased when called twice. Since the function code was relatively simple, these were basic sanity tests. I included these tests in the CI pipeline, so if I ever broke something in the function logic, the CI would catch it before deployment (failing the build).

On the front-end side, my testing was more manual. I would open the website in a browser, ensure the resume content looked right, and that the visitor counter displayed and incremented properly on refresh. I also tested on different devices and in dark mode to make sure everything was legible. One bug I encountered was that the visitor count sometimes didn’t update immediately. This turned out not to be a code bug but a caching issue – Azure Front Door was caching the API responses. The fix was to set proper cache-control headers in the API response so that the function’s output isn’t cached by the CDN. Once I set the response header to `Cache-Control: no-store`, the counter updated on every visit as expected.

Another crucial area of debugging was the **CI/CD pipelines**. Even after getting them to work initially, there were times they failed. For example, one day my front-end deployment workflow started erroring out during the Azure CLI upload. The error message was about an authentication failure. After scratching my head, I realized that the Azure service principal’s secret had expired (by default, Azure AD app secrets can have an expiration). This was an eye-opener – automated credentials need rotation. I generated a new secret, updated the GitHub secret, and all was well. This experience taught me the importance of documenting such caveats and possibly using Azure Managed Identity with GitHub OIDC in the future to avoid secret rotation issues.

I also practiced the skill of reading Azure’s diagnostic logs. For instance, in Azure Functions, I used Application Insights to log each function invocation. In one test, I saw that my function was throwing an exception when two calls came in concurrently. By examining the logs, I pinpointed it to a race condition in my Cosmos DB update (I wasn’t using any concurrency control). While the likelihood of heavy parallel traffic on my resume is low, I still refactored the code to be a bit more robust (I added a retry on failure logic). It was comforting to see the logs clean after that.

**Lesson learned:** **Testing and debugging** are where the rubber meets the road. I learned that having tests is great, but you also need to consider real-world usage (like caching layers, auth expiry) in your verification plan. I developed a more **holistic debugging approach**: not just looking at code, but also at infrastructure, network, and pipeline angles when something went wrong. One of the biggest skills I honed was using logs and error messages to guide my next steps – instead of changing things blindly, I let the evidence from logs lead me to the root cause. This is a crucial skill in any engineering role. Moreover, I gained an appreciation for **failure** – every time something failed, it was an opportunity to make my project more bulletproof. By the end of the challenge, I wasn’t just tolerating failures; I was *embracing* them as part of the learning process.

## Key Takeaways

Completing the Cloud Resume Challenge on Azure was a **transformative experience** for me. Here are some of my key takeaways from this journey:

- **Hands-on Problem Solving:** There’s no substitute for actually building something end-to-end. My problem-solving skills were sharpened daily. When a hurdle appeared (and there were plenty), I learned to break it down, research, and solve it systematically. This project taught me how to learn on-the-fly – whether it was figuring out DNS records or deciphering Terraform error logs – which is a critical skill in the tech industry.

- **Perseverance and Resilience:** There were moments I felt truly stuck or discouraged (I’m looking at you, CI/CD failures at 2 AM). But pushing through those tough moments was incredibly rewarding. I learned to **overcome my own intransigence** – at times I was stubbornly clinging to a wrong approach (Of course there were some situations where I tried to keep a balloon under water), and the challenge forced me to step back and try different angles. Eventually, perseverance paid off. This mindset shift, embracing challenges rather than avoiding them, is something I’ll carry into any job. 

- **Full-Stack Perspective:** Working on this project gave me a 360-degree view of a web application. I dealt with everything from user interface details to database scalability concerns. This holistic understanding is valuable because I can appreciate how things connect: a change in the front-end might require a tweak in the back-end API, which might affect infrastructure or security settings, and so on. It’s made me a more well-rounded engineer.

- **Importance of Documentation and Community:** One of the unsung heroes of my journey was documentation (Azure docs, blog posts, and community forums). I realized the value of reading the fine print. Many solutions came from simply RTFM – “reading the fantastic manual.” Additionally, I lurked in the Cloud Resume Challenge Discord and GitHub discussions; seeing others’ questions and solutions saved me time. The tech community is incredibly helpful, and learning to effectively find and utilize information is a skill in itself.

- **Automation and Best Practices:** By implementing CI/CD and Infrastructure as Code, I ingrained best practices that I will bring to any future projects. Automation not only saves time, but it also enforces consistency and reduces mistakes. I’ve seen first-hand how a solid DevOps pipeline can be the backbone of a project, allowing frequent, reliable updates. This challenge was as much an exercise in DevOps as it was in development.

- **Personal Growth:** On a personal level, finishing this challenge was a huge confidence booster. It served as proof to myself (and hopefully to hiring managers) that I can set a complex goal and see it through. I also learned how to cope with the anxiety of the unknown. At the start, 16 steps looked daunting, but taking them one at a time, I found that *any big problem is solvable if you break it into smaller pieces*. Now, when faced with a new tech problem, I’m far less intimidated because I have a framework to tackle it. 

In summary, the Cloud Resume Challenge was an intense but incredibly educational journey. It strengthened not only my technical competencies in cloud architecture, coding, and automation, but also honed my problem-solving grit and ability to learn independently. I like to say the experience *“catapulted me out of my comfort zone”* — and that’s where real growth happens.

## Call to Action

If you’ve made it this far, thank you for reading my story! I want to leave you with a challenge (and an invitation). **First, I encourage you to take up the Cloud Resume Challenge yourself.** Whether you choose Azure like I did, or AWS or Google Cloud, you will gain hands-on experience that is hard to get from courses or books. It’s not easy – you will struggle – but as I’ve shared, those struggles are exactly what impart the deepest lessons.

For hiring managers or fellow engineers reading this: I invite you to check out my project’s repository on [GitHub](https://github.com/dineshpalli/cloudresumechallenge-azure). There you can see my code, my Terraform scripts, workflow files, and even the history of my commits that document the progression of this project. I’m proud to discuss any part of it. Feel free to quiz me on why I made certain decisions or how I handled a particular problem – I’d love to walk through my thought process. 

Finally, let’s make this a conversation. Have you tried the Cloud Resume Challenge or something similar? Share your experiences or questions in the comments. I’ll be happy to exchange insights or help point aspiring challengers in the right direction if you’re stuck on a step. 

By sharing our learning journeys, we not only celebrate our growth but also inspire others to step up and get their hands dirty (or rather, their keyboards busy!). So, if you’re on the fence, jump in – deploy that website, write that code, configure that pipeline. You’ll come out the other side amazed at what you’ve accomplished. I know I am.

*Thank you for reading, and I hope to see your own cloud resume story soon!* 🚀