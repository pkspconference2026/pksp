# PKSP 2026 Conference Website - Copilot Instructions

## Project Overview
**PKSP 2026** is a conference website for the Malaysian Medical Social Workers Conference 2026 (Persidangan Pegawai Kerja Sosial Perubatan Malaysia).

**Type**: Static HTML website with Firebase backend  
**Deployment**: GitHub Pages (automatic on push to main)  
**Languages**: Malay (ms)

## Project Structure
```
.
├── index.html              # Main conference landing page with registration form
├── admin.html              # Admin dashboard (password-protected) for viewing participants
├── jawatankuasa.html       # Committee/team members page
├── README.md               # Project readme
├── .github/
│   └── workflows/
│       └── static.yml      # GitHub Pages deployment workflow
├── Logo TKPM.png           # Organization logo
├── Logo KKM                # Logo folder
└── Files/                  # (empty - for future use)
```

## Technology Stack

### Frontend
- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first CSS framework
- **Lucide icons** - Icon library
- **AOS** - Animate On Scroll library
- **Language**: Malay (lang="ms")

### Backend Services (Firebase)
- **Firebase Auth** - Anonymous authentication (auto in index.html)
- **Firestore** - Database for participant registrations
- **Firebase Storage** - File uploads (payment proofs, documents)
- **Firebase Config**: Located in index.html `<script type="module">` section

### Deployment
- **GitHub Pages** - Serves entire repository as static site
- **Automatic**: Triggers on push to main branch via `static.yml` workflow

## Key Features

### 1. Registration System (index.html)
- Firebase Firestore integration for participant data
- File upload support for payment proofs via Firebase Storage
- Client-side form validation
- Terms & conditions checkbox requirement
- Real-time participant count display

### 2. Admin Dashboard (admin.html)
- Password-protected access
- Displays all registered participants in table format
- Participant status management (Lulus/Tolak - Approved/Rejected)
- PDF generation capability
- Download functionality for registrations
- No Tailwind CSS - uses custom inline styles for admin panel

### 3. Committee Page (jawatankuasa.html)
- Team members display
- Responsive design using Tailwind CSS
- Custom brand colors (blue, gold, soft, dark)
- Modern typography (Plus Jakarta Sans, Inter fonts)

## Important Notes

### Firebase Configuration
⚠️ **Caution**: The Firebase API key and project ID are visible in index.html source code. This is acceptable for client-side apps but ensure:
- Enable appropriate Firebase Security Rules in Firestore
- Restrict Firebase Storage rules to specific paths
- Use Firebase Authentication to control data access

### Admin Password
- Admin dashboard uses client-side password verification
- Password logic is in admin.html `<script>` section
- For production, consider server-side authentication

### CSS Approach
- **index.html & jawatankuasa.html**: Use Tailwind CSS CDN (dynamic utility classes)
- **admin.html**: Uses inline `<style>` with custom CSS (no framework dependency)

### Deployment Notes
- The entire repository is deployed as-is (path: '.')
- No build step required
- Changes to main branch deploy automatically to GitHub Pages

## Common Development Tasks

### Adding Content
1. For main landing page: Edit `index.html`
2. For committee members: Edit `jawatankuasa.html`
3. For admin features: Edit `admin.html`

### Firebase Modifications
- Import statements at top of `index.html` `<script type="module">`
- Configuration object: `firebaseConfig`
- Collection name: Participants stored in Firestore
- Storage bucket: `pkspconference.firebasestorage.app`

### Styling
- Use Tailwind utility classes in index.html and jawatankuasa.html
- For admin.html, modify `<style>` section directly
- Brand colors: `#1e3a8a` (blue), `#c5a059` (gold), `#0f172a` (dark)

### Testing
- Open HTML files in browser directly
- Firebase requires internet connectivity
- Test file uploads in Chrome DevTools Network tab

## Localization
- All UI text is in Malay (ms)
- Font support for CJK characters via Google Fonts
- Date/time formatting should use locale-aware methods

## Git & Deployment
- Push to `main` branch to trigger automatic GitHub Pages deployment
- Workflow file: `.github/workflows/static.yml`
- No manual deployment needed
- Check GitHub Actions tab for deployment status

## Next Steps / Improvement Ideas
- Server-side admin password verification
- Email confirmation for registrations
- SMS notifications
- Participant statistics dashboard
- Calendar integration for conference schedule
- Payment gateway integration (currently manual proof upload)
