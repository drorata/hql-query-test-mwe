# How to use Pytest to unit test queries

On MacOS, you'd like to install Java, maybe as follow:

```bash
brew tap adoptopenjdk/openjdk
brew cask install adoptopenjdk8
```

Next, you'd need to have Java in your path:

```bash
export JAVA_HOME=$(/usr/libexec/java_home)
```

Now, you can run the test:

```bash
pytest
```
