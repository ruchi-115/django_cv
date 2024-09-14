from django.shortcuts import render

def cv_view(request):
    context = {
        'name': 'Ruchita Sonawale',
        'profession': 'New York, NY',
        'email': 'rs9230@nyu.edu',
        'linkedin': 'https://linkedin.com/in/ruchita-sonawale/',
        'github': 'https://github.com/ruchi-115',
        'educations': [
            {
                'degree': 'Master of Computer Science',
                'field': '',
                'school': 'New York University, Tandon School of Engineering',
                'start_year': 'Sept 2024',
                'end_year': 'May 2026',
                'cgpa': ''
            },
            {
                'degree': 'Bachelor of Engineering - Computer Engineering',
                'field': '',
                'school': 'Datta Meghe College of Engineering, University of Mumbai',
                'start_year': 'Aug 2020',
                'end_year': 'June 2024',
                'cgpa': '9.36/10'
            }
        ],
        'work_experiences': [
            {
                'title': 'Software Intern',
                'company': 'TechnoHacks Edutech Ltd.',
                'start_date': 'Aug 2023',
                'end_date': 'Sept 2023',
                'description': 'Successfully executed 3+ projects, demonstrating advanced proficiency in both front-end and back-end technologies using Next.js for dynamic user interfaces, while adhering to Scrum/Agile methodologies. Implemented a functional login system and integrated RESTful APIs for seamless payment processing, optimizing database management and significantly improving user interactions and system efficiency by 30%.'
            },
            {
                'title': 'Web Developer Intern',
                'company': 'Lets Grow More',
                'start_date': 'Sept 2021',
                'end_date': 'Oct 2021',
                'description': 'Designed single-page applications using React.js and MongoDB, demonstrating a strong grasp of core software engineering principles and modern web technologies. Developed three websites, utilizing web responsive design, resulting 40% increase in engagement & quality code. Led the end-to-end development process from concept to deployment, gaining hands-on experience.'
            }
        ],
        'projects': [
            {
                'title': 'ZEB: E-commerce Platform',
                'description': 'Constructed a comprehensive full-stack e-commerce platform using Django, implementing a robust authentication system with django-allauth that significantly enhanced user security and streamlined the login/signup process. Integrated SQLite for efficient database management, improving order tracking and delivery processes, while incorporating the PayPal Payment Gateway to secure transactions.'
            },
            {
                'title': 'Wildlife Detection and Evaluation from Camera-Trap Images Using Deep Learning',
                'description': 'Developed an advanced object detection model using Detectron 2 based on PyTorch, achieving 89% accuracy in identifying and segmenting 14 wildlife species from over 1,000 camera-trap images. Utilized deep learning techniques to improve counting and classification of individual animals, resulting in a 30% increase in the accuracy of wildlife population estimates and aiding in conservation efforts. Delivered a fully functional web application that streamlined the process of species identification and data analysis, reducing research time by 40% and enhancing the efficiency of wildlife monitoring initiatives.'
            },
            {
                'title': 'Ideacon: A Collaborative Platform for Sharing and Discussing Innovative Ideas',
                'description': 'Developed a full-stack application using Next.js, enabling users to share and discuss innovative ideas in a collaborative environment with seamless frontend and backend integration. Engineered a responsive and visually appealing user interface using React.js, HTML, and CSS, while managing backend operations with MongoDB and Next.js, ensuring robust data storage and retrieval capabilities. Secured the platform with Auth0, integrating Google login to provide users with secure authentication process.'
            }
        ],
        'leaderships': [
            {
                'title': 'Technical Team, CATT - CSI DMCE',
                'start_date': 'April 2021',
                'end_date': 'Aug 2023',
                'description': 'Organized 10+ competitive technical workshops, with various projects to promote open sourcing on GitHub. Designed a full-stack web application using Figma, React and PostgreSQL for events.'
            },
            {
                'title': 'Web Dev Team, Google Developer Students Club (GDSC) DMCE',
                'start_date': 'Sept 2021',
                'end_date': 'Aug 2022',
                'description': 'Contributed to GDSC community by hosting events and contributing to projects with 500+ community students. Worked on the main committee website using 3D models and three.js, and learned new frameworks.'
            }
        ],
        'skills': [
            'Python', 'C++', 'C', 'SQL', 'HTML', 'CSS', 'JavaScript', 'React', 'Bootstrap', 'Tailwind', 'Flask', 'Django', 'Next.js', 'Node.js', 'Blender', 'Figma', 'Three.js', 'CS50', 'CS50Web', 'Git', 'VSCode', 'PyCharm', 'GitHub', 'MS Office'
        ],
        'awards': [
            'Published “Visual Question Answering (VQA) with CLIP Model” in IJRASET, Vol. 12, Issue IV, April 2024.',
            '1st Prize Winner Smart India Hackathon 2022 (SIH) - National Level Hackathon conducted by Gov. of India.',
            'Awarded Indian Patent "An Iron Ore Supply Chain Monitoring System and Method," published on June 2, 2023.',
            'Won 1st Place at PRISM 2022, a research hackathon with Indo Korea Science and Technology Centre (IKST).'
        ]
    }
    return render(request, 'home.html', context)
