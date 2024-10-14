# To do list
1. Choose backend and frontend frameworks

Best choice seems to be `FastAPI` for the backend and `React` for frontend. The backend and frontend should be deployed in separate containers and the frontend will make calls to the backend API.

Backend features
- user authentication and account management
    - data management: create, store and manange user accounts
    - authorization: only authorized users can access certain resources
- payments via stripe
    - secure payment processing
    - webhook handling
    - subscription management
- file upload and processing
    - store files securely on cloud
    - preprocessing files: extract text from PDFs
    - API integration (openai)
- analysis results storage
    - database: users can view and manage past uploads
- subscription and usage control
    - enforce subscription limits
    - auditing and analytics


2. Setup environment with docker
3. Upload the docker image to google cloud and setup a container with a custom domain
4. Add user database and UI for login / register
5. Add file database and let user upload documents to it from the UI

