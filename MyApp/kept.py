from flask import render_template,flash,url_for,redirect,request
from MyApp import app,db
from MyApp.forms import HomeForm,PlayForm,ReplayForm,ReplayOptionForm,TryAgainForm
import random
from MyApp.models import Details,Number
from collections import defaultdict


value = {}

@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    form = HomeForm()
    number=random.randint(1,20)
    if form.validate_on_submit():
        db.drop_all()
        db.create_all()
        details = Details(name=form.name.data, score=0)
        db.session.add(details)
        db.session.commit()
        number = Number(number=number)
        db.session.add(number)
        db.session.commit()
        flash(f'Random number-->{number} has been generated!','success')
        return redirect(url_for('playGame'))  
    return render_template('home.html', title='Home', form=form)

@app.route("/playGame",methods=['GET', 'POST'])
def playGame():
    detail = Details.query.first()
    number = Number.query.first()
    form = PlayForm()
    if 'count' in value:
        value['count'] +=1
        count = value['count'] 
    else:
        value['count'] =0
        count = value['count'] 
    if form.validate_on_submit():
        number = number.number
        name = detail.name
        if int(form.number.data) == number:
            score = detail.score
            detail.score = score + 50
            db.session.commit()
            score = detail.score
            flash(f'{name}, {form.number.data} was the right number! Your total score now is ===>{score}') 
            return redirect(url_for('replay_option',number=number))
        else:
            while value['count']<5:
                if int(form.number.data)>number:
                    flash(f'{form.number.data} was too high.Try again. You have tried {count} times', 'danger')
                    return redirect(url_for('playGame'))
                elif int(form.number.data)<number:
                    flash(f'{form.number.data} was too low. Try again. You have tried {count} times', 'danger')
                    return redirect(url_for('playGame'))
                value['count']+=1
            else:
                value.clear() #clear dict when trial ends and a new game is started
                return redirect(url_for('try_again'))
    return render_template('playGame.html', title='playgame',form=form)


@app.route("/replay_option",methods=['GET', 'POST'])
def replay_option(): 
    form = ReplayOptionForm()
    number= random.randint(1,20)
    num = Number.query.first()
    num.number=number
    db.session.commit()
    return render_template('replay_option.html',title='replay_option',form = form)


@app.route("/replay",methods=['GET', 'POST'])
def replay():
    detail = Details.query.first()
    number = Number.query.first()
    form = ReplayForm()
    if form.validate_on_submit():
        number = number.number
        name = detail.name
        if int(form.number.data) == number:
            score = detail.score
            detail.score = score + 50
            db.session.commit()
            score = detail.score
            flash(f'{name}, {form.number.data} was the right number! Your total score now is ===>{score}') 
            return redirect(url_for('replay_option')) 
        else:
            if int(form.number.data)>number:
                flash(f'{form.number.data} was too high. Try again.', 'danger')
                return redirect(url_for('playGame'))
            elif int(form.number.data)<number:
                flash(f'{form.number.data} was too low. Try again.', 'danger')
                return redirect(url_for('playGame'))
    flash(f'Random number-->{number} has been generated!','success')
    return render_template('replay.html', title='replaygame',form=form)

@app.route("/try_again",methods=['GET', 'POST'])
def try_again(): 
    form = TryAgainForm()
    return render_template('try_again.html',title='home',form = form)


@app.route("/exit")
def exit():
    return render_template('exit.html')


  