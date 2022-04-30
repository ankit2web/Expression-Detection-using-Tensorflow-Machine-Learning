# Expression Detection using Tensorflow (Machine Learning)

#### How to setup the environment to use this project ?

1. Download & Install 64 bit of [Python3](https://www.python.org/) on your system from.

2. Once python is installed, download virtualenv package on your system. To do that open any terminal window on your system (CMD/Powershell on Windows) & type `python -m pip install virtualenv`

3. Now create a virtual environment in the project's root directory to hold all the required dependencies needed to execute this project. To do that, navigate to root of this project & open a terminal window over there & then type `python -m virtualenv venv`

4. Activate the virtual environment

- On windows : `venv\Scripts\activate`
- On mac/linux : `source venv/bin/activate`

5. Virtual environment will be activated & `(venv)` will start appearing in your terminal window indicating successful activation of the virtual environment

6. Install project dependencies, `pip install -r requirements.txt`

7. Now all required packages will be installed.

8. Now run ROI.py : `python ROI.py`

9. Train the CNN Model using test dataset : `python TrainCNNModel.py`

10. Start init script after all train epochs are completed : `python ExpressionInit.py`

11. It should now open a camera window which will detect Expressions of any person present in front of it, Cheers !!
