# 🚀 Deployment Guide

## Option 1: Streamlit Community Cloud (Recommended - FREE & Easiest)

Streamlit Community Cloud is the official free hosting platform for Streamlit apps. It's the easiest and best option for your app.

### Steps:

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Sign up for Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy your app**
   - Click "New app"
   - Select your GitHub repository
   - Choose the branch (usually `main`)
   - Set the main file path: `Forest FIre Prediction/app.py`
   - Click "Deploy"

4. **Wait for deployment** (usually takes 1-2 minutes)

5. **Your app will be live** at: `https://your-app-name.streamlit.app`

### Important Notes:
- Make sure `model.pkl` and `requirements.txt` are in the same directory as `app.py`
- The app will automatically install dependencies from `requirements.txt`
- Free tier includes unlimited apps and public hosting

---

## Option 2: Deploy to Vercel (Advanced - Not Recommended for Streamlit)

⚠️ **Important**: Vercel is designed for static sites and serverless functions, not persistent Python applications like Streamlit. To deploy Streamlit to Vercel, you'll need to use Docker containers or convert to a different architecture.

### Using Vercel with Docker (Complex):

1. **Create a `Dockerfile`**:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY "Forest FIre Prediction/requirements.txt" .
RUN pip install --no-cache-dir -r requirements.txt

COPY "Forest FIre Prediction" .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. **Create `vercel.json`**:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "Dockerfile",
      "use": "@vercel/docker"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/"
    }
  ]
}
```

3. **Deploy**:
   - Install Vercel CLI: `npm i -g vercel`
   - Run: `vercel --prod`

⚠️ **Limitations with Vercel**:
- Streamlit apps need persistent WebSocket connections, which may not work well on Vercel
- Cold starts can be slow
- May have timeout issues with long-running processes
- Not officially supported by Streamlit

---

## Option 3: Other Deployment Platforms (Recommended Alternatives)

### Render (Easy & Free)
- Sign up at [render.com](https://render.com)
- Create a new "Web Service"
- Connect your GitHub repo
- Set build command: `pip install -r requirements.txt`
- Set start command: `streamlit run app.py --server.port=$PORT`
- Free tier available

### Railway (Easy & Free)
- Sign up at [railway.app](https://railway.app)
- Create a new project from GitHub
- Add a start command: `streamlit run "Forest FIre Prediction/app.py" --server.port=$PORT`
- Free tier available

### Heroku (Paid after free tier ended)
- Uses `Procfile` and requires additional setup
- Not recommended due to removal of free tier

---

## Recommendation

**Use Streamlit Community Cloud** - it's free, easy, officially supported, and designed specifically for Streamlit apps. It will give you the best experience with minimal configuration.
