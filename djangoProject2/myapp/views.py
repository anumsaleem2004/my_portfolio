from django.shortcuts import render, redirect
from .models import Skill, Project, Education, Experience, Certification, Tool

def add_skills(request):
    if request.method == 'POST':
        # Handle skill form submission
        if 'skill_name' in request.POST:
            skill_name = request.POST.get('skill_name')
            if skill_name:
                Skill.objects.create(name=skill_name)


        # Handle project form submission
        elif 'project_name' in request.POST:
            project_name = request.POST.get('project_name')
            project_description = request.POST.get('project_description')
            if project_name and project_description:
                Project.objects.create(title=project_name, description=project_description)

        # Handle education form submission
        elif 'degree' in request.POST:
            degree = request.POST.get('degree')
            institution = request.POST.get('institution')
            year = request.POST.get('year')
            if degree and institution and year:
                Education.objects.create(title=degree, description=institution, year=year)

        # Handle experience form submission
        elif 'position' in request.POST:
            position = request.POST.get('position')
            company = request.POST.get('company')
            duration = request.POST.get('duration')
            end_date = request.POST.get('end_date')
            descripton = request.POST.get('des')
            if position and company and duration and end_date and descripton:
                Experience.objects.create(title=position, company=company, start_date=duration,end_date=end_date, descripton=descripton)

        # Handle certification form submission
        elif 'cert_name' in request.POST:
            cert_name = request.POST.get('cert_name')
            issuer = request.POST.get('issuer')
            if cert_name and issuer:
                Certification.objects.create(title=cert_name, description=issuer)

        # Handle tool form submission
        elif 'tool_name' in request.POST:
            tool_name = request.POST.get('tool_name')
            if 'tool_logo' in request.FILES:
                tool_logo = request.FILES['tool_logo']
            else:
                tool_logo = None
            if tool_name:
                Tool.objects.create(name=tool_name, logo=tool_logo)

        return redirect('skills')  # Redirect to the same page to clear the form and show the updated list

    # Fetch all data from the database
    context = {
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'education': Education.objects.all(),
        'experience': Experience.objects.all(),
        'certifications': Certification.objects.all(),
        'tools': Tool.objects.all(),
    }

    return render(request, 'skills.html', context)

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    certifications = Certification.objects.all()
    tools = Tool.objects.all()

    context = {
        'skills': skills,
        'projects': projects,
        'education': education,
        'experience': experience,
        'certifications': certifications,
        'tools': tools,
    }

    return render(request, 'home.html', context)

def delete_skills(request):
    if request.method == 'POST':
        skill_ids = request.POST.getlist('skills_to_delete')
        Skill.objects.filter(id__in=skill_ids).delete()
    return redirect('skills')
# Deleting projects
def delete_projects(request):
    if request.method == 'POST':
        project_ids = request.POST.getlist('projects_to_delete')
        Project.objects.filter(id__in=project_ids).delete()
    return redirect('skills')

# Deleting education
def delete_education(request):
    if request.method == 'POST':
        education_ids = request.POST.getlist('education_to_delete')
        Education.objects.filter(id__in=education_ids).delete()
    return redirect('skills')

# Deleting experience
def delete_experience(request):
    if request.method == 'POST':
        experience_ids = request.POST.getlist('experience_to_delete')
        Experience.objects.filter(id__in=experience_ids).delete()
    return redirect('skills')

# Deleting certifications
def delete_certifications(request):
    if request.method == 'POST':
        certification_ids = request.POST.getlist('certifications_to_delete')
        Certification.objects.filter(id__in=certification_ids).delete()
    return redirect('skills')

# Deleting tools
def delete_tools(request):
    if request.method == 'POST':
        tool_ids = request.POST.getlist('tools_to_delete')
        Tool.objects.filter(id__in=tool_ids).delete()
    return redirect('skills')