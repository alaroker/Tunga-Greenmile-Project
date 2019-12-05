# app/home/views.py

from flask import render_template
from flask_login import login_required
from flask import abort, render_template, request
from flask_login import current_user, login_required

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
      result = request.form
      return render_template("index2.html",result = result)

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")


# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")

###############################################################################
###############################################################################

# add admin dashboard view
@home.route('/supplier/dashboard')
@login_required
def supplier_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_supplier:
        abort(403)

    return render_template('home/supplier_dashboard.html', title="Dashboard")

#######################################################################################
#######################################################################################

# add admin dashboard view
@home.route('/loader/dashboard')
@login_required
def loader_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_loader:
        abort(403)

    return render_template('home/loader_dashboard.html', title="Dashboard")

#################################################################################
#################################################################################

# add admin dashboard view
@home.route('/recipient/dashboard')
@login_required
def recipient_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_recipient:
        abort(403)

    return render_template('home/recipient_dashboard.html', title="Dashboard")