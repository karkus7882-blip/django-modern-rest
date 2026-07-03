# 🌐 How to Access Your GameHub Web App on Different IP Addresses

## Quick Overview

When you run `python manage.py runserver`, Django only listens on `127.0.0.1:8000` by default. Here's how to access it from:
- ✅ Your local machine (localhost)
- ✅ Other devices on your network
- ✅ Public internet (with proper setup)

---

## 🖥️ Method 1: Access on Local Machine (Easiest)

### Option A: Using localhost
```bash
# Terminal
python manage.py runserver

# Browser
http://localhost:8000
http://127.0.0.1:8000
```

### Option B: Using your machine's hostname
```bash
# Get your machine name
hostname

# In browser, use:
http://YOURMACHINENAME.local:8000
# Example: http://MacBook-Pro.local:8000
```

---

## 🌍 Method 2: Access from Other Devices on Same Network

### Step 1: Find Your Local IP Address

**On Windows:**
```bash
ipconfig
# Look for "IPv4 Address" under "Ethernet adapter" or "Wireless LAN adapter"
# Example: 192.168.1.100
```

**On macOS/Linux:**
```bash
ifconfig
# or
hostname -I
# Look for 192.168.x.x or 10.0.x.x
```

**Or use this Python one-liner:**
```bash
python -c "import socket; print(socket.gethostbyname(socket.gethostname()))"
```

### Step 2: Run Django on Your IP Address

```bash
# Instead of default localhost, bind to 0.0.0.0
python manage.py runserver 0.0.0.0:8000

# Or specify your exact IP
python manage.py runserver 192.168.1.100:8000
```

### Step 3: Access from Another Device

On any device on your network (phone, laptop, tablet):
```
http://192.168.1.100:8000
http://YOUR_IP_ADDRESS:8000
```

**Example URLs:**
```
http://192.168.1.100:8000/
http://10.0.0.5:8000/
http://172.16.0.10:8000/
```

---

## 🚀 Method 3: Complete Setup for Network Access

### Step 1: Update Django Settings

Edit `django_test_app/server/settings.py`:

```python
# Allow all local network IPs
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '*',  # DANGER: Only for development!
    # Or specify exact IPs:
    '192.168.1.100',
    '192.168.1.101',
]
```

### Step 2: Run with Proper Configuration

```bash
# From django_test_app directory
python manage.py runserver 0.0.0.0:8000
```

### Step 3: Find Your IP and Test

**Quick IP finder script** (`find_ip.py`):
```python
import socket

def get_local_ip():
    """Get local IP address"""
    try:
        # Create a socket connection to a public server
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception:
        return "127.0.0.1"

if __name__ == "__main__":
    ip = get_local_ip()
    print(f"🌐 Access your app at: http://{ip}:8000")
    print(f"   From this machine: http://localhost:8000")
    print(f"   From other devices: http://{ip}:8000")
```

Run it:
```bash
python find_ip.py
# Output:
# 🌐 Access your app at: http://192.168.1.100:8000
#    From this machine: http://localhost:8000
#    From other devices: http://192.168.1.100:8000
```

---

## 🔒 Method 4: Access from Public Internet (Advanced)

### Option A: Using ngrok (Free Tunneling)

```bash
# Install ngrok
brew install ngrok  # macOS
# or download from https://ngrok.com

# Start your Django app
python manage.py runserver

# In another terminal, create a tunnel
ngrok http 8000

# You'll get a public URL like:
# https://abc123def456.ngrok.io
```

### Option B: Using Flask-Sockets or Expose

```bash
# Install expose
pip install expose

# Run expose
expose http://localhost:8000
```

### Option C: Port Forwarding on Router

⚠️ **Advanced & Security Risk!** Only do this if you know what you're doing.

1. Log into your router
2. Find Port Forwarding settings
3. Forward external port 8000 → internal IP 192.168.1.100:8000
4. Find your public IP: https://whatismyipaddress.com
5. Access: `http://YOUR_PUBLIC_IP:8000`

---

## 📱 Method 5: Testing on Mobile Devices

### iPhone/iPad on Same Network

1. Find your IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Run: `python manage.py runserver 0.0.0.0:8000`
3. On phone, open Safari and go to: `http://192.168.1.100:8000`

### Android on Same Network

1. Same as iPhone
2. Open Chrome and go to: `http://192.168.1.100:8000`

### Using QR Code Generator

Generate QR code for easy mobile access:

```bash
# Install qrcode
pip install qrcode[pil]

# Create script (qr_generator.py)
import qrcode

ip = "192.168.1.100"
url = f"http://{ip}:8000"

qr = qrcode.QRCode()
qr.add_data(url)
qr.make()
qr.print_ascii()

print(f"\n🔗 Scan this QR code or visit: {url}")
```

Run it:
```bash
python qr_generator.py
```

---

## 📊 Quick Reference Table

| Access Type | Command | URL |
|------------|---------|-----|
| **Local Machine** | `python manage.py runserver` | `http://localhost:8000` |
| **Local Network** | `python manage.py runserver 0.0.0.0:8000` | `http://192.168.1.100:8000` |
| **Specific IP** | `python manage.py runserver 192.168.1.100:8000` | `http://192.168.1.100:8000` |
| **Different Port** | `python manage.py runserver 0.0.0.0:3000` | `http://192.168.1.100:3000` |
| **Public Internet** | `ngrok http 8000` | `https://abc123.ngrok.io` |

---

## 🔥 Common Issues & Solutions

### ❌ "Connection Refused"
```bash
# Make sure Django is running
python manage.py runserver 0.0.0.0:8000

# Check if port 8000 is in use
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows
```

### ❌ "Address already in use"
```bash
# Use different port
python manage.py runserver 0.0.0.0:3000
```

### ❌ "DisallowedHost error"
```python
# Update ALLOWED_HOSTS in settings.py
ALLOWED_HOSTS = ['*']  # Development only!
```

### ❌ "Can't reach from other device"
```bash
# Check:
1. Both devices on same network
2. Firewall not blocking port 8000
3. Using correct IP (not localhost)
4. Django running on 0.0.0.0
```

---

## 🛡️ Security Warnings

⚠️ **Development Only!**

```python
# NEVER use in production:
DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'insecure-key'

# For production, use:
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
# Deploy with Gunicorn/Uvicorn behind Nginx
```

---

## 🚀 Production Deployment

### Using Gunicorn (Recommended)

```bash
pip install gunicorn

# Run on all interfaces
gunicorn \
  --bind 0.0.0.0:8000 \
  --workers 4 \
  server.wsgi:application

# Access at: http://YOUR_IP:8000
```

### Using Uvicorn (Async)

```bash
pip install uvicorn

# Run on all interfaces
uvicorn \
  --host 0.0.0.0 \
  --port 8000 \
  server.asgi:application

# Access at: http://YOUR_IP:8000
```

### Using Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server.wsgi:application"]
```

Build and run:
```bash
docker build -t gamehub .
docker run -p 8000:8000 gamehub

# Access at: http://localhost:8000 or http://YOUR_IP:8000
```

---

## 📝 Useful Commands Reference

```bash
# Get local IP
python -c "import socket; print(socket.gethostbyname(socket.gethostname()))"

# Run on specific IP and port
python manage.py runserver 192.168.1.100:3000

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000

# Check if port is in use
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process on port
kill -9 $(lsof -t -i :8000)  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

---

## ✅ Step-by-Step for Network Access

1. **Find your IP:**
   ```bash
   python -c "import socket; print(socket.gethostbyname(socket.gethostname()))"
   ```

2. **Update ALLOWED_HOSTS** in `settings.py`:
   ```python
   ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.100']
   ```

3. **Start Django:**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

4. **Open browser:**
   ```
   http://192.168.1.100:8000
   ```

Done! 🎉

---

**Need Help?** Check the [GameHub Setup Guide](./GAMEHUB_SETUP.md)
