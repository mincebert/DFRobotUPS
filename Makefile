all: DFRobotUPS

.PHONY: remake DFRobotUPS upload clean


remake: clean all

DFRobotUPS:
	./setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/*

clean:
	rm -rf build dist DFRobotUPS.egg-info
