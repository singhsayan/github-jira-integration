# GitHub → Jira Integration using Flask & AWS EC2

This project demonstrates how to automatically create Jira issues when specific events occur in a GitHub repository.  
The integration is powered by a Flask application hosted on AWS EC2, with GitHub Webhooks triggering Jira REST API calls.

---

## Tech Stack
- **Backend Framework:** Flask (Python)
- **Hosting:** AWS EC2 (Ubuntu)
- **Integration:** Jira REST API
- **Trigger:** GitHub Webhook
- **Authentication:** Jira API Token (generated automatically by the Flask app when `/jira` is called)

---

## Workflow Overview
1. **GitHub Webhook** sends a `POST` request to the Flask server running on EC2.
2. Flask processes the payload and **automatically generates a Jira API token**.
3. The Flask app uses the token to call the **Jira REST API**.
4. Jira creates a **new issue** in the specified project.

---

## Step-by-Step Setup

### 1. Launch AWS EC2 Instance
1. Open **AWS Console** → Go to **EC2** → Click **Launch Instance**.
2. Choose **Ubuntu** as the OS.
3. Configure **Security Group**:
   - **Port 5000** (Flask app)
   - **Port 22** (SSH access)
4. Launch the instance and connect via SSH:
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-public-ip
   ```

**Example EC2 Terminal Connection:**  
![EC2 Terminal](Screenshot/ec2-terminal.png)

---

### 2. Install Python & Create Virtual Environment
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Required Python Packages
```bash
pip install flask requests
```

---

### 4. Create a Jira Project
1. Log in to your Jira account.
2. Navigate: **Projects → Create Project**.
3. Choose a template (**Scrum**, **Kanban**, or **Bug Tracking**).
4. Assign a **name** and **project key** (e.g., `AB`).
5. Save the project — you'll need the **key** in your Flask app.

---

### 5. Configure GitHub Webhook
1. Go to your **GitHub repository → Settings → Webhooks**.
2. Click **Add Webhook**.
3. Set:
   - **Payload URL:** `http://<EC2-Public-IPv4-DNS>:5000/createJira`
   - **Content type:** `application/json`
4. Select **events** you want to trigger Jira issue creation (select **Issues**).
5. Save the webhook.

**Webhook Delivery Example:**  
![Webhook Delivery](Screenshot/webhook-delivery.png)

---

### 6. Run the Flask App
```bash
python your_file_name.py
```
Your app will now:
- Listen for incoming GitHub events
- Automatically generate a Jira API token
- Create Jira issues based on the webhook payload

---

**Jira Token got created:**
![Jira Token](Screenshot/jira-token.png)

## Post-Project Cleanup
To avoid unnecessary charges and maintain security:
- **Delete AWS EC2 Instance**:  
  Go to **AWS EC2 → Instances → Select → Terminate**.
- **Revoke Jira API Token** (if stored for re-use):  
  Go to [Jira API Token Management](https://id.atlassian.com/manage/api-tokens) → **Revoke** the token.

---

## Summary
This integration enables seamless automation between GitHub and Jira, making project management more efficient.  
By hosting the Flask app on EC2 and leveraging GitHub Webhooks, you can turn code events into actionable Jira issues instantly — with API tokens generated automatically during the process.

---
