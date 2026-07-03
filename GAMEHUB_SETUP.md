# 🎮 GameHub Setup & Running Guide

## Quick Start - Run GameHub Now!

### Prerequisites
- Python 3.11+
- Django 5.0+
- pip or uv package manager

### Step 1: Clone & Setup

```bash
# Clone your fork
git clone https://github.com/karkus7882-blip/django-modern-rest.git
cd django-modern-rest

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django django-modern-rest

# Or with all dev dependencies
pip install -e ".[pydantic,msgspec,jwt,openapi]"
```

### Step 2: Update Django Settings

Add `game_hub` to `INSTALLED_APPS` in `django_test_app/server/settings.py`:

```python
INSTALLED_APPS = [
    # ... existing apps ...
    'server.apps.game_hub',
    # ... rest of apps ...
]
```

### Step 3: Update URL Configuration

Add GameHub route to `django_test_app/server/urls.py`:

```python
from django.urls import include, path

# Add this import at the top
from server.apps.game_hub import urls as game_hub_urls

# Then in urlpatterns, add:
urlpatterns = [
    path('', include(game_hub_urls.urls, namespace='game_hub')),
    # ... existing routes ...
]
```

### Step 4: Run Development Server

```bash
cd django_test_app
python manage.py runserver
```

### Step 5: Access the App

Open your browser and navigate to:
```
http://localhost:8000/
```

🎉 **You should now see the GameHub app running with all HTML5 & CSS3 features!**

---

## 🌟 Features Showcase

### HTML5 Features
✅ **Semantic Elements**
- `<header>` - Sticky navigation bar
- `<main>` - Main content area
- `<article>` - Game cards grid
- `<section>` - Featured collections
- `<figure>` & `<figcaption>` - Image captions
- `<nav>` - Bottom navigation
- `<footer>` - Footer navigation
- `<details>` & `<summary>` - Expandable collections

✅ **Responsive Images**
- `<picture>` element for responsive image sources
- Lazy loading with `loading="lazy"`
- Automatic fallback for different screen sizes

✅ **Accessibility**
- ARIA labels on all interactive elements
- Keyboard navigation support
- Focus states for all buttons and links
- Semantic HTML for screen readers

### CSS3 Features
✨ **Advanced Layouts**
- CSS Grid for responsive game cards
- Flexbox for flexible component layouts
- Aspect ratios for consistent card dimensions

✨ **Animations & Transitions**
- Gradient animations (8s loop)
- Floating button animation (3s loop)
- Hover scale & transform effects
- Pulse effects on badges
- Smooth transitions (0.3s cubic-bezier)

✨ **Modern CSS**
- CSS Custom Properties (variables)
- Backdrop filters (glass morphism effect)
- Linear & radial gradients
- Will-change optimization
- Media queries for responsiveness

✨ **Visual Effects**
- Box shadows with emerald glow
- Gradient overlays on images
- Smooth color transitions
- Rounded corners with borders

---

## 📂 Project Structure

```
django_test_app/
├── server/
│   ├── apps/
│   │   ├── game_hub/           # ← GameHub App
│   │   │   ├── __init__.py
│   │   │   ├── apps.py         # App config
│   │   │   ├── views.py        # HTML5/CSS3 view
│   │   │   └── urls.py         # URL routing
│   │   ├── controllers/
│   │   ├── middlewares/
│   │   └── ...
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL config
│   └── wsgi.py
└── manage.py
```

---

## 🧪 Testing the App

### Test Responsive Design
1. Open DevTools (F12)
2. Toggle Device Toolbar (Ctrl+Shift+M)
3. Try different screen sizes
4. Observe grid layout adapting

### Test Animations
- Hover over game cards → Scale & shadow effects
- Check floating plus button → Continuous animation
- Click details sections → Expandable content

### Test Accessibility
- Press Tab → Navigate through all interactive elements
- Use screen reader → All elements have proper labels
- High contrast mode → Still fully readable

### Test Performance
```bash
# In browser DevTools:
# Lighthouse → Run audit
# Look for: Performance, Accessibility, Best Practices scores
```

---

## 🚀 Deployment

### Using Gunicorn (Sync)
```bash
pip install gunicorn
gunicorn server.wsgi:application --bind 0.0.0.0:8000
```

### Using Uvicorn (Async)
```bash
pip install uvicorn
uvicorn server.asgi:application --host 0.0.0.0 --port 8000
```

### Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["gunicorn", "server.wsgi:application", "--bind", "0.0.0.0:8000"]
```

---

## 📚 Resources

- **django-modern-rest**: https://django-modern-rest.rtfd.io
- **HTML5 Spec**: https://html.spec.whatwg.org/
- **CSS3 Guide**: https://developer.mozilla.org/en-US/docs/Web/CSS
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Font Awesome Icons**: https://fontawesome.com/docs

---

## 🐛 Troubleshooting

### Issue: "No module named 'server.apps.game_hub'"
**Solution**: Ensure `INSTALLED_APPS` includes `'server.apps.game_hub'`

### Issue: CSS not loading
**Solution**: 
- Ensure Tailwind CDN is accessible
- Check browser console for errors
- Clear browser cache (Ctrl+Shift+Delete)

### Issue: Images not showing
**Solution**:
- Check internet connection (images from picsum.photos)
- Verify `loading="lazy"` attribute is present
- Check CORS headers if using image proxy

### Issue: Port 8000 already in use
**Solution**: 
```bash
# Use different port
python manage.py runserver 8001
```

---

## 📝 Code Examples

### Using HTML5 Picture Element
```html
<picture>
  <source media="(min-width: 768px)" srcset="large.jpg">
  <img src="small.jpg" alt="Responsive image" loading="lazy">
</picture>
```

### CSS3 Gradient Animation
```css
.gradient-animated {
  background: linear-gradient(45deg, #10b981, #06b6d4, #10b981);
  background-size: 300% 300%;
  animation: gradientShift 8s ease infinite;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
```

### CSS3 Backdrop Filter (Glass Morphism)
```css
.glass-effect {
  backdrop-filter: blur(10px);
  background: rgba(24, 24, 27, 0.7);
  border: 1px solid rgba(39, 39, 42, 0.5);
}
```

---

## 🎯 Next Steps

1. **Customize Colors**: Edit CSS custom properties in `:root`
2. **Add More Games**: Duplicate game card HTML
3. **Connect Backend**: Add Django views for game data
4. **Database Integration**: Use Django ORM models
5. **API Integration**: Use django-modern-rest for REST endpoints

---

## 📞 Support

For issues with:
- **GameHub App**: Check this file
- **django-modern-rest**: See [Parent Repository Issues](#parent-repo-issues)
- **HTML5/CSS3**: See MDN documentation links above

Happy coding! 🚀
