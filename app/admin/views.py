# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
# from . forms import PackageForm
from .. import db
# from ..models import Package

from . forms import PackageForm, LoaderAssignForm
from ..models import Package, User


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:

        abort(403)

# Department Views


@admin.route('/packages', methods=['GET', 'POST'])
@login_required
def list_packages():
    """
    List all packages
    """
    check_admin()

    packages = Package.query.all()

    return render_template('admin/packages/packages.html',
                           packages=packages, title="Packages")


@admin.route('/packages/add', methods=['GET', 'POST'])
@login_required
def add_package():
    """
     Add a package to the database
    """
    check_admin()

    add_package = True

    form = PackageForm()
    if form.validate_on_submit():
        package = Package(name=form.name.data, date_created = form.date_created.data, date_to_deliver = form.date_to_deliver.data,
        addressed_to = form.addressed_to.data, package_type = form.package_type.data, hub = form.hub.data,
                                description=form.description.data,)
        # try:
            # add department to the database
        db.session.add(package)
        db.session.commit()
        flash('You have successfully added a new package.')
        # except:
            # in case department name already exists
            # flash('Error: package name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_packages'))

    # load department template
    return render_template('admin/packages/package.html', action="Add",
                           add_package=add_package, form=form,
                           title="Add Package")


@admin.route('/packages/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_package(id):
    """
    Edit a package
    """
    check_admin()

    add_package = False

    package = Package.query.get_or_404(id)
    form = PackageForm(obj=package)
    if form.validate_on_submit():
        package.name = form.name.data
        package.date_created = form.date_created.data
        package.date_to_deliver = form.date_to_deliver.data
        package.addressed_to = form.addressed_to.data
        package.package_type = form.package_type.data
        package.hub = form.hub.data
        package.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the package.')

        # redirect to the departments page
        return redirect(url_for('admin.list_packages'))

    
    form.name.data = package.name
    form.date_created.data = package.date_created
    form.date_to_deliver.data = package.date_to_deliver
    form.addressed_to.data = package.addressed_to
    form.package_type.data = package.package_type
    form.hub.data = package.hub
    form.description.data = package.description
    return render_template('admin/packages/package.html', action="Edit",
                           add_package=add_package, form=form,
                           package=package, title="Edit Package")


@admin.route('/packages/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_package(id):
    """
    Delete a package from the database
    """
    check_admin()

    package = Package.query.get_or_404(id)
    db.session.delete(package)
    db.session.commit()
    flash('You have successfully deleted the package.')

    # redirect to the departments page
    return redirect(url_for('admin.list_packages'))

    return render_template(title="Delete Package")  

# Loader Views

@admin.route('/loaders')
@login_required
def list_loaders():
    """
    List all employees
    """
    check_admin()

    loaders = User.query.all()
    return render_template('admin/loaders/loaders.html',
                           loaders=loaders, title='Loaders')


@admin.route('/loaders/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_loaders(id):
    """
    Assign a department and a role to an employee
    """
    check_admin()

    loader = User.query.get_or_404(id)

    # prevent admin from being assigned a department or role
    if loader.is_admin:
        abort(403)
    elif loader.is_supplier:
        abort(403)

    form = LoaderAssignForm(obj=loader)
    if form.validate_on_submit():
        loader.package = form.package.data 
        
        db.session.add(loader)
        db.session.commit()
        flash('You have successfully assigned a package.')

        # redirect to the roles page
        return redirect(url_for('admin.list_loaders'))

    return render_template('admin/loaders/loader.html',
                           loader=loader, form=form,
                           title='Assign Loader')