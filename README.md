# Sanji90 CRM 
 
A simple, free, Zoho-like CRM built with Streamlit, SQLite, and Plotly. 
 
## Features 
- **Auth**: Sign up, login, logout. 
- **Dashboard**: Overview of leads, contacts, deals, tasks. 
- **Leads**: Create, view, update, delete leads. 
- **Contacts**: Manage contact details. 
- **Deals**: Track deals by stage (Open, Won, Lost). 
- **Tasks**: Assign and manage tasks. 
- **Reports**: Visualize lead and deal data with Plotly charts. 
- **Settings**: Update password and logout. 
 
## Setup 
1. Clone the repo: 
   ```bash 
   git clone <your-repo-url> 
   cd sanji90-crm 
   ``` 
2. Install dependencies: 
   ```bash 
   pip install -r requirements.txt 
   ``` 
3. Run the app locally: 
   ```bash 
   streamlit run app.py 
   ``` 
4. Access at `http://localhost:8501`. 
 
## Deployment 
- **Render**: Use the free tier. Create a `render.yaml`: 
  ```yaml 
  services: 
    - type: web 
      name: sanji90-crm 
      env: python 
      plan: free 
      buildCommand: pip install -r requirements.txt 
      startCommand: streamlit run app.py --server.port $PORT 
  ``` 
- Push to GitHub and deploy via Render's dashboard. 
 
## Color Scheme 
- Red (#FF4500) 
- Black (#1C2526) 
- White (#FFFFFF) 
- Orange (#FF6347) 
 
## Notes 
- Runs entirely locally with SQLite. 
- No paid services required. 
- Scalable for future features (e.g., email integration, APIs). 
