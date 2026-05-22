# One-Click Build Setup

## What you get
- A Run button inside GitHub (Actions tab → Run workflow)
- Auto-rebuild every day at 6am UTC (keeps TODAY date fresh)
- Auto-rebuild on every push to main

## Steps

### 1. Add the workflow file
In your repo `brightlane/HalloweenCostumes`, create this folder structure:

```
.github/
  workflows/
    build.yml    ← paste the content from build.yml
```

### 2. Make sure GitHub Pages is enabled
- Go to repo Settings → Pages
- Source: Deploy from branch → main → / (root)
- Save

### 3. Allow Actions to push back to the repo
- Go to repo Settings → Actions → General
- Scroll to "Workflow permissions"
- Select "Read and write permissions"
- Save

### 4. Run it manually (the Run button)
- Go to your repo on GitHub
- Click the "Actions" tab
- Click "🎃 Build Halloween Site" in the left sidebar
- Click "Run workflow" dropdown → "Run workflow"
- Watch it build all 130+ pages live

### 5. After that it runs itself
Every push to main triggers a rebuild.
Every morning at 6am UTC it rebuilds automatically (updates the date on every page).

## The Run Button location
GitHub → your repo → Actions tab → "🎃 Build Halloween Site" → "Run workflow" button
