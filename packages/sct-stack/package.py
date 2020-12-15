from spack import *
from spack.main import get_version
import spack.architecture as architecture
from datetime import datetime
import os
import platform
import llnl.util.tty as tty
import spack.user_environment as uenv
from spack.pkg.k4.Ilcsoftpackage import k4_add_latest_commit_as_dependency 
from spack.pkg.k4.Ilcsoftpackage import k4_generate_setup_script 
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage


class SctStack(BundlePackage, Key4hepPackage):
    """Bundle package to install the Key4hep software stack."""
    
    homepage = 'https://cern.ch/key4hep'

    ##################### versions ########################
    #######################################################
    # tries to build the HEAD of each package.
    # used for master builds
    version('master')
    # the preferred usage is to use the date as versio, like: 
    # builds the latest stable version of each package
    # the preferred usage is to use the date as version, see below
    #version('master-2020-10-06')
    version(datetime.today().strftime('%Y-%m-%d'))
    #version('2020-10-06') # example, no need to add them here

    phases = ['install']

    ##################### variants ########################
    #######################################################
    variant('devtools', default=True,
            description="add tools necessary for software masterment to the stack")
    variant('generators', default=False,
            description="add some standalone generators to the stack")
    variant('bootstrap', default=False,
            description="install some spack setup tools")
    

    ##################### common key4hep packages #########
    #######################################################
    depends_on('edm4hep')
    k4_add_latest_commit_as_dependency("edm4hep", "key4hep/edm4hep", when="@master")

    depends_on('podio')
    #k4_add_latest_commit_as_dependency("podio", "aidasoft/podio", when="@master")
    depends_on("podio@master", when="@master")

    depends_on("k4fwcore")
    k4_add_latest_commit_as_dependency("k4fwcore", "key4hep/k4fwcore", when="@master")

    depends_on("k4simdelphes")
    k4_add_latest_commit_as_dependency("k4simdelphes", "key4hep/k4simdelphes", when="@master")
    
    depends_on("guinea-pig")
    # todo: figure out the api for the cern gitlab instance
    #depends_on('guinea-pig@master', when="@master")

    depends_on('whizard +lcio +openloops hepmc=2')
    # todo: figure out the api for the whizard gitlab instance
    #depends_on('whizard@master +lcio +openloops hepmc=2', when="@master")

    depends_on("delphes")
    #k4_add_latest_commit_as_dependency("delphes", "delphes/delphes", when="@master")
    depends_on("delphes@master", when="@master")

    ##################### general purpose generators ######
    #######################################################
    depends_on("madgraph5amc", when="+generators")
    depends_on("herwigpp", when="+generators")
    # todo: investigate build failure with newer versions
    depends_on("lhapdf@6.2.3", when="+generators")



    ############################### ilcsoft ###############
    #######################################################
    depends_on('aidatt')
    k4_add_latest_commit_as_dependency("aidatt", "aidasoft/aidatt", when="@master")

    depends_on('cedviewer')
    k4_add_latest_commit_as_dependency("cedviewer", "ilcsoft/cedviewer", when="@master")

    depends_on('conformaltracking')
    k4_add_latest_commit_as_dependency("conformaltracking", "ilcsoft/conformaltracking", when="@master")

    depends_on('clicperformance')
    k4_add_latest_commit_as_dependency("clicperformance", "ilcsoft/clicperformance", when="@master")

    depends_on('clupatra')
    k4_add_latest_commit_as_dependency("clupatra", "ilcsoft/clupatra", when="@master")

    depends_on('ced')
    k4_add_latest_commit_as_dependency("ced", "ilcsoft/ced", when="@master")

    depends_on('ddkaltest')
    k4_add_latest_commit_as_dependency("ddkaltest", "ilcsoft/ddkaltest", when="@master")

    depends_on('ddmarlinpandora')
    k4_add_latest_commit_as_dependency("ddmarlinpandora", "ilcsoft/ddmarlinpandora", when="@master")

    depends_on('fcalclusterer')
    k4_add_latest_commit_as_dependency("fcalclusterer", "fcalsw/fcalclusterer", when="@master")

    depends_on('forwardtracking')
    k4_add_latest_commit_as_dependency("forwardtracking", "ilcsoft/forwardtracking", when="@master")

    depends_on('garlic')
    k4_add_latest_commit_as_dependency("garlic", "ilcsoft/garlic", when="@master")

    depends_on('k4marlinwrapper')
    k4_add_latest_commit_as_dependency("k4marlinwrapper", "key4hep/k4marlinwrapper", when="@master")

    depends_on('generalbrokenlines')
    k4_add_latest_commit_as_dependency("generalbrokenlines", "GeneralBrokenLines/GeneralBrokenLines", when="@master")

    depends_on('gear')
    k4_add_latest_commit_as_dependency("gear", "ilcsoft/gear", when="@master")

    depends_on('ilcutil')
    k4_add_latest_commit_as_dependency("ilcutil", "ilcsoft/ilcutil", when="@master")

    depends_on('ildperformance')
    k4_add_latest_commit_as_dependency("ildperformance", "ilcsoft/ildperformance", when="@master")

    depends_on('kaldet')
    k4_add_latest_commit_as_dependency("kaldet", "ilcsoft/kaldet", when="@master")

    depends_on('kitrackmarlin')
    k4_add_latest_commit_as_dependency("kitrackmarlin", "ilcsoft/kitrackmarlin", when="@master")

    depends_on('kaltest')
    k4_add_latest_commit_as_dependency("kaltest", "ilcsoft/kaltest", when="@master")

    depends_on('kitrack')
    k4_add_latest_commit_as_dependency("kitrack", "ilcsoft/kitrack", when="@master")

    depends_on('lcfiplus')
    k4_add_latest_commit_as_dependency("lcfiplus", "lcfiplus/lcfiplus", when="@master")

    depends_on('lctuple')
    k4_add_latest_commit_as_dependency("lctuple", "ilcsoft/lctuple", when="@master")

    depends_on('lcfivertex')
    k4_add_latest_commit_as_dependency("lcfivertex", "ilcsoft/lcfivertex", when="@master")

    depends_on('lich')
    k4_add_latest_commit_as_dependency("lich", "danerdaner/lich", when="@master")

    depends_on('lccd')
    k4_add_latest_commit_as_dependency("lccd", "ilcsoft/lccd", when="@master")

    depends_on('lcio')
    #k4_add_latest_commit_as_dependency("lcio", "ilcsoft/lcio", when="@master")
    #depends_on("lcio@master", when="@master")

    depends_on('lcgeo')
    k4_add_latest_commit_as_dependency("lcgeo", "ilcsoft/lcgeo", when="@master")

    depends_on('marlin')
    k4_add_latest_commit_as_dependency("marlin", "ilcsoft/marlin", when="@master")

    depends_on('marlinutil')
    k4_add_latest_commit_as_dependency("marlinutil", "ilcsoft/marlinutil", when="@master")

    depends_on('marlinpandora')
    k4_add_latest_commit_as_dependency("marlinpandora", "pandorapfa/marlinpandora", when="@master")

    depends_on("marlindd4hep")
    k4_add_latest_commit_as_dependency("marlindd4hep", "ilcsoft/marlindd4hep", when="@master")

    depends_on('marlinreco')
    k4_add_latest_commit_as_dependency("marlinreco", "ilcsoft/marlinreco", when="@master")

    depends_on('marlinfastjet')
    k4_add_latest_commit_as_dependency("marlinfastjet", "ilcsoft/marlinfastjet", when="@master")

    depends_on('marlinkinfit')
    k4_add_latest_commit_as_dependency("marlinkinfit", "ilcsoft/marlinkinfit", when="@master")

    depends_on('marlintrkprocessors')
    k4_add_latest_commit_as_dependency("marlintrkprocessors", "ilcsoft/marlintrkprocessors", when="@master")

    depends_on('marlintrk')
    k4_add_latest_commit_as_dependency("marlintrk", "ilcsoft/marlintrk", when="@master")

    depends_on('overlay')
    k4_add_latest_commit_as_dependency("overlay", "ilcsoft/overlay", when="@master")

    depends_on('pandoraanalysis')
    k4_add_latest_commit_as_dependency("pandoraanalysis", "PandoraPFA/LCPandoraAnalysis", when="@master")

    depends_on('pandorapfa')
    k4_add_latest_commit_as_dependency("pandorapfa", "pandorapfa/pandorapfa", when="@master")


    depends_on('physsim')
    k4_add_latest_commit_as_dependency("physsim", "ilcsoft/physsim", when="@master")

    depends_on("raida")
    k4_add_latest_commit_as_dependency("raida", "ilcsoft/raida", when="@master")

    depends_on('sio')
    #k4_add_latest_commit_as_dependency("sio", "ilcsoft/sio", when="@master")


    ############################### fccsw #################
    #######################################################
    # depends_on("fccsw")
    # k4_add_latest_commit_as_dependency("fccsw", "hep-fcc/fccsw", when="@master")

    # depends_on("fcc-edm")
    # k4_add_latest_commit_as_dependency("fcc-edm", "hep-fcc/fcc-edm", when="@master")

    #depends_on("dual-readout")
    #k4_add_latest_commit_as_dependency("dual-readout", "hep-fcc/dual-readout", when="@master")

    # depends_on("fccanalyses")

    ############################## cepcsw #################
    #######################################################
    depends_on("cepcsw")
    k4_add_latest_commit_as_dependency("cepcsw", "cepc/cepcsw", when="@master")
    
    depends_on("k4lcioreader")
    k4_add_latest_commit_as_dependency("k4lcioreader", "key4hep/k4LCIOReader", when="@master")


    ##################### SCT Framework ###################
    #######################################################
    def LCG_external_package_(package_version='', everything=[]):
        #print(package_version)
        package_version = package_version.strip()
        while "  "  in package_version:
            package_version = package_version.replace("  ", " ")
        splitted = package_version.split(" ", 1)
        if len(splitted) == 2:
            package, version = splitted[0], splitted[1]
            dependent = "%s@%s" % (package.strip(), version.strip())
        else:
            dependent = splitted[0]
        #print(dependent)
        everything.append(dependent)
        depends_on(dependent)

    everything = []
    from functools import partial
    LCG_external_package = partial(LCG_external_package_, everything=everything)
    LCG_external_package("py-astroid           2.0.4                                    ")
    # ADDME LCG_external_package("control           0.7.0                                    ")
    LCG_external_package("py-ipython")#           7.8.0                                    ")
    LCG_external_package("py-paramiko          2.4.0                                    ")
    LCG_external_package("py-pylint            2.1.1                                    ")
    LCG_external_package("py-pyserial          3.4                                      ")
    LCG_external_package("python            3.7.9                                    ")
    # ADDME LCG_external_package("python_vxi11      0.9                                      ")
    LCG_external_package("redis             2.10.6                                   ")
    LCG_external_package("py-spyder")#            3.2.4                                    ")
    # ADDME LCG_external_package("typed_ast         1.4.1                                    ")
    LCG_external_package("py-prompt-toolkit    2.0.10                                   ")
    #LCG_external_package("root_numpy        4.8.0                                    ")
    LCG_external_package("py-tensorflow")#        1.13.0                                   ")
    LCG_external_package("py-iminuit           1.4.9                                    ")
    # ADDME LCG_external_package("probfit           1.1.0                                    ")
    LCG_external_package("py-numpy             ")#1.19.4                                   ")
    LCG_external_package("py-ipykernel         5.1.2                                    ")
    LCG_external_package("py-pybind11          2.6.0                                    ")

    # LCG_AA_project("RELAX  root6   ")
    # LCG_AA_project("ROOT   6.22.02 ")
    # LCG_AA_project("HepMC  3.2.2   ")
    depends_on("geant4@10.06 cxxstd=17")
    # LCG_AA_project("DD4hep 1.14.01 ")

    # ADDME LCG_external_package("lcgenv            1.3.8                                    ")
    LCG_external_package("py-4suite-xml            1.0.2p1                                  ")
    LCG_external_package("py-absl-py           0.2.2:                                    ")
    LCG_external_package("acts         2.00.0                                  ")
    LCG_external_package("aida              3.2.1                                    ")
    LCG_external_package("aidatt            0.10                                     ")
    #LCG_external_package("astor             0.8.1                                    ")
    LCG_external_package("py-atomicwrites      1.1.5                                    ")
    LCG_external_package("py-attrs             18.1.0:                                   ")
    LCG_external_package("autoconf          2.69:                                     ")
    LCG_external_package("automake          1.16.1:                                   ")
    LCG_external_package("py-backcall          0.1.0                                    ")
    LCG_external_package("blas              0.3.9.openblas                           ")
    LCG_external_package("py-bleach            2.1.3                                    ")
    LCG_external_package("boost             1.70.0                                   ")
    LCG_external_package("r-c50               2.07                                     ")
    LCG_external_package("cairo             1.15.8+X                                   ")
    # ADDME LCG_external_package("catboost        0.9.1.1                                  ")

    LCG_external_package("ccache            3.3.4                                    ")
    LCG_external_package("ced               1.09.03                                  ")
    LCG_external_package("py-certifi           2018.4.16                                ")
    LCG_external_package("py-chardet           3.0.4                                    ")
    # ADDME LCG_external_package("cfe               8.0.1                                    ")
    depends_on("clhep@2.4.1.0 cxxstd=17")
    LCG_external_package("py-click             6.7                                      ")
    LCG_external_package("py-cloudpickle       0.5.3                                    ")
    LCG_external_package("clupatra          1.03                                     ")
    LCG_external_package("cmake             3.14.3                                   ")
    LCG_external_package("hsf-cmaketools        1.6                                      ")
    # ADDME LCG_external_package("cmmnbuild         2.1.3                                    ")
    LCG_external_package("coin3d            3.1.3p2                                  ")
    LCG_external_package("conddbmysql       0.9.7                                    ")
    LCG_external_package("py-configparser      3.5.0                                    ")
    LCG_external_package("couchdb           1.2                                      ")
    LCG_external_package("py-coverage          4.5.1                                    ")
    LCG_external_package("cppgsl            1.0.0                                    ")
    # ADDME_LCG_external_package("cppitertools      master20201111                           ")
    # ADDME LCG_external_package("cpplint           1.4.3                                    ")
    LCG_external_package("cppunit           1.12.1_p1  ")#               author=1.12.1  ")
    # ADDME LCG_external_package("cpymad            1.0.8                                    ")
    LCG_external_package("curl            7.59.0                                   ")
    # FIXME LCG_external_package("cx_oracle         6.4.1                                    ")
    LCG_external_package("py-cycler            0.10.0                                   ")
    LCG_external_package("py-cython            0.29.21                                  ")
    LCG_external_package("py-dask              0.18.1                                   ")
    LCG_external_package("davix           0.6.7:                                    ")  # for root
    LCG_external_package("ddkaltest         1.06                                     ")
    LCG_external_package("py-decorator         4.3.0                                    ")
    LCG_external_package("delphes           3.4.3pre06                                    ")
    LCG_external_package("py-dill              0.3.1                                  ")
    LCG_external_package("py-distributed       1.22.0                                   ")
    LCG_external_package("doxygen           1.8.11                                   ")
    LCG_external_package("edm4hep           0.3                                     ")
    LCG_external_package("eigen             3.3.4                                    ")
    LCG_external_package("elasticsearch     6.3.0                                    ")
    LCG_external_package("py-entrypoints       0.2.3                                    ")
    LCG_external_package("expat             2.2.5                                    ")
    LCG_external_package("fastjet           3.3.0                                    ")
    LCG_external_package("fftw              3.3.4 ")#                    fftw3          ")
    LCG_external_package("fjcontrib         1.030                                    ")
    LCG_external_package("flatbuffers       1.12.0                                   ")
    LCG_external_package("fmt               7.1.2                                    ")
    LCG_external_package("fontconfig        2.12.6                                   ")
    #LCG_external_package("fplll             5.0.3                                    ")
    LCG_external_package("freeglut          3.0.0                                    ")
    LCG_external_package("freetype          2.6.3                                    ")
    # ADDME LCG_external_package("ftjam             2.5.2                                    ")
    LCG_external_package("py-funcsigs          1.0.2                                    ")
    LCG_external_package("py-future            0.16.0                                   ")
    # NOT NEEDED FOR PY3LCG_external_package("py-futures           3.2.0                                    ")
    # ADDME LCG_external_package("garfieldpp        master20191018                           ")
    LCG_external_package("py-gast              0.2.0:                                    ")
    LCG_external_package("generalbrokenlines               2.1.3                                    ")
    LCG_external_package("gdb             9.2                                      ")
    LCG_external_package("gear              1.09                                     ")
    # ADDME LCG_external_package("genfit            20200306                                 ")
    LCG_external_package("py-genshi            0.7                                      ")
    LCG_external_package("geos              3.6.2                                    ")
    LCG_external_package("gettext           0.19.8.1                                 ")
    LCG_external_package("glew              2.1.0                                    ")
    LCG_external_package("glib              2.58.3                                   ")
    LCG_external_package("gmp               6.0.0                                    ")
    LCG_external_package("tar              1.30                                     ")
    LCG_external_package("sed              4.5                                      ")
    LCG_external_package("gperf             3.1                                      ")
    LCG_external_package("gperftools      2.5                                      ")
    LCG_external_package("graphviz          2.28.0                                   ")
    LCG_external_package("py-grpcio            1.33.2                                   ")
    LCG_external_package("gsl               2.5                                      ")
    # ADDME LCG_external_package("gtest             master20160308                           ")
    LCG_external_package("py-h5py              2.8.0:                                    ")
    LCG_external_package("harfbuzz          1.6.3                                    ")
    LCG_external_package("hdf5              1.8.18:                                   ")
    LCG_external_package("py-heapdict          1.0.0:                                    ")
    # ADDME LCG_external_package("hepdata_converter 0.1.32                                   ")
    LCG_external_package("py-hepdata-validator 0.1.16                                   ")
    LCG_external_package("heppdt            3.04.01                                  ")
    LCG_external_package("py-html5lib          1.0.1                                    ")
    LCG_external_package("py-idna              2.7                                      ")
    LCG_external_package("ilcutil           1.06                                     ")
    LCG_external_package("py-ipaddress         1.0.22                                   ")
    LCG_external_package("py-ipython-genutils  0.2.0                                    ")
    LCG_external_package("py-ipywidgets        7.3.0                                    ")
    LCG_external_package("py-isort             4.3.4                                    ")
    # LCG_external_package("java              8u91                                     ")
    LCG_external_package("jdk              1.8                                     ")
    LCG_external_package("py-jedi ")#             0.12.1                                   ")
    LCG_external_package("jemalloc          4.1.0                                    ")
    LCG_external_package("py-jinja2            2.10:                                     ")
    LCG_external_package("py-joblib            0.17.0                                   ")
    LCG_external_package("py-jpype1             0.6.2                                    ")
    LCG_external_package("json-c             0.12                                     ")
    LCG_external_package("jsoncpp           1.7.2                                    ")
    LCG_external_package("py-jsonschema        2.6.0                                    ")
    LCG_external_package("py-jupyter           1.0.0                                    ")
    # ADDM LCG_external_package("jupyter_client    5.2.3                                    ")
    # ADDM LCG_external_package("jupyter_console   5.2.0                                    ")
    # ADDM LCG_external_package("jupyter_contrib_core 0.3.3                                 ")
    # ADDM LCG_external_package("jupyter_contrib_nbextensions 0.5.0                         ")
    # ADDM LCG_external_package("jupyter_core      4.4.0                                    ")
    # ADDM LCG_external_package("jupyter_highlight_selected_word 0.2.0                      ")
    # ADDM LCG_external_package("jupyter_latex_envs 1.4.4                                   ")
    # ADDM LCG_external_package("jupyter_nbextensions_configurator 0.4.0                    ")
    LCG_external_package("kaldet            1.14.01                                  ")
    LCG_external_package("kaltest           2.05                                     ")
    LCG_external_package("py-keras             2.2.0                                    ")
    LCG_external_package("py-keras-applications 1.0.8:                                   ")
    LCG_external_package("py-keras-preprocessing 1.1.0:                                  ")
    # ADDME LCG_external_package("kiwisolver        1.0.1                                    ")
    LCG_external_package("kitrack           1.10                                     ")
    LCG_external_package("kitrackmarlin     1.13                                     ")
    LCG_external_package("lapack            3.9.0                                    ")
    # ADDME LCG_external_package("lazy_object_proxy 1.3.1                                    ")
    LCG_external_package("lccd              1.05                                     ")
    LCG_external_package("lcio              2.13.01                                  ")
    LCG_external_package("lcgeo             0.16.05                                  ")
    LCG_external_package("lcov              1.9                                      ")
    LCG_external_package("libaio            0.3.110-1                                ")
    LCG_external_package("libdrm            2.4.103                                  ")
    LCG_external_package("libepoxy          1.5.4                                    ")
    LCG_external_package("libffi            3.2.1                                    ")
    LCG_external_package("libgit2           0.27.0                                   ")
    LCG_external_package("libsvm            2.86                                     ")
    LCG_external_package("libtool           2.4.2                                    ")
    LCG_external_package("libxkbcommon    0.7.1                                    ")
    LCG_external_package("libxml2           2.9.7                                    ")
    LCG_external_package("libxslt           1.1.28                                   ")
    LCG_external_package("llvm              8.0.1                                    ")
    # ADDME LCG_external_package("logilabcommon     1.4.2                                    ")
    # ADDME LCG_external_package("lxml              4.6.1                                    ")
    # ADDME LCG_external_package("py-m2crypto        0.30.1                                   ")
    LCG_external_package("m4                1.4.18                                   ")
    # ADDME LCG_external_package("madx              5.04.02                                  ")
    LCG_external_package("py-mako              1.1.2                                    ")
    LCG_external_package("py-markdown          3.1.1                                   ")
    LCG_external_package("py-markupsafe        1.1.1                                    ")
    LCG_external_package("marlin            1.17                                     ")
    LCG_external_package("marlintrk         2.08                                     ")
    LCG_external_package("marlintrkprocessors         2.11                           ")
    LCG_external_package("marlinutil        1.15.01                                  ")
    LCG_external_package("py-matplotlib        2.2.2                                    ")
    LCG_external_package("py-mccabe            0.6.1                                    ")
    LCG_external_package("mesa              20.2.2                                   ")
    LCG_external_package("mesa-glu          9.0.1                                    ")
    LCG_external_package("mesa-demos        8.4.0                                    ")
    LCG_external_package("meson             0.53.2                                   ")
    # ADDME LCG_external_package("py-messaging         1.1                                      ")
    # ADDME LCG_external_package("py-metakernel        0.20.14                                  ")
    LCG_external_package("py-minrpc            0.0.10                                   ")
    LCG_external_package("py-mistune           0.8.3                                    ")
    LCG_external_package("py-mock              2.0.0                                    ")
    LCG_external_package("py-more-itertools    4.2.0                                    ")
    LCG_external_package("motif             2.3.8                                    ")
    LCG_external_package("mpifileutils              1.5.1                                    ")  # FIXME?
    LCG_external_package("mpfr              3.1.5                                    ")
    LCG_external_package("py-mpmath            1.0.0                                    ")
    # ADDME LCG_external_package("msgpack           0.5.6                                    ")
    LCG_external_package("py-multiprocess      0.70.11.1                                 ")
    # ADDME? LCG_external_package("py-multiprocessing   2.6.2.1                                  ")
    LCG_external_package("mysql             5.7.25: cxxstd=17 +client_only ") # each version requires different boost, let version float
    LCG_external_package("py-pymysql      1.2.5                                    ") # FIXME?
    LCG_external_package("nanomsg           1.1.3                                    ")
    LCG_external_package("py-nbconvert         5.3.1                                    ")
    LCG_external_package("py-nbformat          4.4.0                                    ")
    LCG_external_package("py-networkx          2.1                                      ")
    LCG_external_package("ninja             1.7.2.gcc0ea.kitware.dyndep              ")
    LCG_external_package("py-nose              1.3.7                                    ")
    LCG_external_package("py-notebook          5.6.0                                    ")
    LCG_external_package("py-numexpr           2.6.6                                    ")
    # ADDME LCG_external_package("omniorb           4.2.2                                    ")
    LCG_external_package("openmpi           3.1.0                                    ")
    LCG_external_package("openssl         1.1.0h                                   ")
    # ADDME LCG_external_package("oracle            11.2.0.3.0                               ")
    LCG_external_package("overlay           0.22                                     ")
    # ADDME LCG_external_package("pacparser         1.3.5                                    ")
    LCG_external_package("py-pandas            1.1.4                                    ")
    LCG_external_package("py-pandocfilters     1.4.2                                    ")
    LCG_external_package("pango             1.40.13+X                                  ")
    LCG_external_package("py-parso             0.3.1                                    ")
    LCG_external_package("py-pathlib2          2.3.2                                    ")
    LCG_external_package("py-pathos            0.2.2.1                                  ")
    LCG_external_package("py-patsy             0.5.0                                    ")
    LCG_external_package("py-pbr               4.1.1                                    ")
    LCG_external_package("pcre              8.38                                     ")
    LCG_external_package("py-pexpect           4.6.0                                    ")
    LCG_external_package("py-pickleshare       0.7.4                                    ")
    LCG_external_package("py-pip               10.0.1                                   ")
    LCG_external_package("pixman            0.34.0                                   ")
    #LCG_external_package("pjlsa             0.0.13                                   ")
    LCG_external_package("pkg-config        0.28                                     ")
    LCG_external_package("pkgconfig         1.4.0                                    ")
    LCG_external_package("py-pluggy            0.6.0                                    ")
    LCG_external_package("libpng               1.6.17                                   ")
    #LCG_external_package("podio             0.12                                     ")
    LCG_external_package("py-pox               0.2.5                                    ")
    LCG_external_package("py-ppft              1.6.4.9                                  ")
    # ADDME LCG_external_package("prctl           1.7                                      ")
    LCG_external_package("py-prettytable       0.7.2                                    ")
    # ADDME LCG_external_package("processing        0.52                                     ")  # not neeed for py3?
    LCG_external_package("py-prometheus-client 0.3.0                                    ")
    LCG_external_package("protobuf          2.5.0:                                    ")
    LCG_external_package("py-psutil            5.4.6                                    ")
    LCG_external_package("py-ptyprocess        0.6.0                                    ")
    LCG_external_package("py-py                1.5.4                                    ")
    LCG_external_package("py-py2neo            4.0.0                                    ")

    LCG_external_package("py-py4j              0.10.7                                   ")
    # ADDME LCG_external_package("pyanalysis        2.0                                      ")
    LCG_external_package("py-pydot             1.2.4                                    ")
    # ADDME LCG_external_package("pydot_ng          1.0.0                                    ")
    LCG_external_package("py-pygments          2.2.0                                    ")
    # NEEDS PY2 LCG_external_package("py-gsi           0.6.3                                    ")
    # ADDME LCG_external_package("pyjapc            1.5.6                                    ")
    LCG_external_package("py-pyparsing         2.2.0                                    ")
    # ADDME LCG_external_package("pystan            2.17.1.0                                 ")
    LCG_external_package("py-pytest            3.6.3                                    ")
    LCG_external_package("py-pytest-runner     4.2                                      ")
    LCG_external_package("py-python-dateutil   2.7.3                                    ")
    LCG_external_package("py-python-gitlab     0.20                                     ")
    # ADDME LCG_external_package("pytimber          2.6.2                                    ")
    LCG_external_package("py-pytools           2.0                                      ")
    LCG_external_package("py-pytz              2018.5                                   ")
    # ADDME WHICH PYXML? LCG_external_package("pyxml             0.8.4p1                                  ")
    LCG_external_package("py-pyyaml            3.13                  ")#            pyyaml ")
    LCG_external_package("py-pyzmq             19.0.2                                   ")

    #LCG_external_package("qt                4.8.7                 ")#    qt             ")
    LCG_external_package("py-qtconsole         4.3.1                                    ")
    LCG_external_package("r                 3.2.5:+X                                    ")
    LCG_external_package("raida             1.9                                      ")
    LCG_external_package("range-v3           0.10.0 cxxstd=17                                   ")
    LCG_external_package("readline          7.0                                      ")
    LCG_external_package("py-requests          2.24.0                                   ") # For tensorboard
    LCG_external_package("py-rise              5.3.0                                    ")
    #LCG_external_package("rootpy            1.0.1                                    ")
    LCG_external_package("py-rpy2              2.8.6                                    ")
    LCG_external_package("py-scandir           1.10.0                                   ")
    LCG_external_package("py-scikit-learn       0.19.2                                   ")
    LCG_external_package("py-scipy             1.5.4                                    ")
    LCG_external_package("py-seaborn           0.9.0                                    ")
    LCG_external_package("py-send2trash        1.5.0                                    ")
    LCG_external_package("py-setuptools        41.0.0                                   ") # For tensorboard
    LCG_external_package("py-setuptools-scm    3.1.0                                    ")
    LCG_external_package("py-shapely           1.6.4.post2                              ")
    LCG_external_package("py-simplegeneric     0.8.1                                    ")
    LCG_external_package("py-simplejson        3.16.0                                   ")
    LCG_external_package("py-singledispatch    3.4.0.3                                  ")
    LCG_external_package("py-six               1.11.0:                                   ")
    #LCG_external_package("sollya            6.0                                      ")
    LCG_external_package("py-sortedcontainers  2.0.4                                    ")
    LCG_external_package("spdlog            1.2.0                                    ")
    LCG_external_package("py-sqlalchemy        1.2.10                                   ")
    LCG_external_package("sqlite            3210000                                  ")
    LCG_external_package("py-statsmodels       0.9.0                                    ")
    # ADDME LCG_external_package("py-stomppy           3.1.3                                    ")
    LCG_external_package("storm             0.20                                     ")
    LCG_external_package("py-subprocess32      3.5.2                                    ")
    LCG_external_package("swig              3.0.12          ")#author=3.0.12            ")
    LCG_external_package("py-sympy             1.2                                      ")
    LCG_external_package("tbb               2019_U1                                  ")
    LCG_external_package("py-tblib             1.3.2                                    ")
    LCG_external_package("py-tensorboard       1.12.0          ")#protobuf=3.6.1           ")
    LCG_external_package("py-termcolor         1.1.0                                    ")
    LCG_external_package("py-terminado         0.8.1                                    ")
    LCG_external_package("py-testpath          0.3.1                                    ")
    LCG_external_package("texinfo           6.3                                      ")
    LCG_external_package("py-theano            1.0.2                                    ")
    LCG_external_package("py-toolz             0.9.0                                    ")
    LCG_external_package("py-tornado           5.1                                      ")
    LCG_external_package("py-traitlets         4.3.2                                    ")
    LCG_external_package("tricktrack        1.0.9                                    ")
    #LCG_external_package("umesimd           0.8.1                                    ")
    LCG_external_package("py-urllib3           1.23                                     ")
    LCG_external_package("uuid              1.42                                     ")
    LCG_external_package("valgrind        3.13.0                                   ")
    LCG_external_package("vc                1.3.2                                    ")
    LCG_external_package("py-vcversioner       2.16.0.0                                 ")
    LCG_external_package("vdt               0.3.9                                    ")
    #LCG_external_package("vectorclass       1.30                                     ")
    LCG_external_package("py-wcwidth           0.1.7                                    ")
    LCG_external_package("py-webencodings      0.5.1                                    ")
    LCG_external_package("py-werkzeug          0.14.1                                   ")
    LCG_external_package("py-wheel             0.31.1                                   ")
    LCG_external_package("py-widgetsnbextension 3.3.0                                   ")
    LCG_external_package("py-wrapt             1.10.11:                                  ")
    LCG_external_package("xapian-core            1.2.21                                   ")
    LCG_external_package("xerces-c           3.2.3 ")#       author=3.2.3                ")
    LCG_external_package("py-xenv              master20201111                           ")
    LCG_external_package("xgboost           0.71                                     ")
    LCG_external_package("xqilla            2.3.3                                    ")
    LCG_external_package("xrootd            4.10.0+python                                   ")
    #LCG_external_package("xrootd_python   0.3.0                                    ")
    LCG_external_package("yaml-cpp           0.5.4                                    ")
    LCG_external_package("py-yapf              0.29.0                                   ")
    # ADDME LCG_external_package("zeromq            4.2.5                                    ")
    #LCG_external_package("zict              0.1.3                                    ")
    LCG_external_package("zlib              1.2.11                                   ")



    # for aThing in everything:
    #     others = ''
    #     for other in everything:
    #         if aThing != other:
    #             others += ' ^' + other
    #     print(aThing + others)
        

    ##################### developer tools #################
    #######################################################
    depends_on("cmake", when="+devtools")
    depends_on("gdb", "when=+devtools")
    depends_on("emacs+X toolkit=athena", when="+devtools")
    depends_on("ninja", when="+devtools")
    depends_on("py-ipython", when="+devtools")
    depends_on("doxygen", when="+devtools")
    depends_on('py-particle', when="+devtools")
    depends_on('py-awkward1', when="+devtools")
    depends_on('py-matplotlib', when="+devtools")
    depends_on('py-uproot4', when="+devtools")
    #depends_on('py-tensorflow') # todo: check if we should integrate.
    #depends_on('py-zfit') # todo: add in spack



    ##################### environment boostrap ############
    #######################################################
    depends_on("environment-modules", when="+bootstrap")


    ##################### conflicts #######################
    #######################################################
    conflicts("%gcc@8.3.1",
              msg="There are known issues with compilers from redhat's devtoolsets" \
              "which are therefore not supported." \
              "See https://root-forum.cern.ch/t/devtoolset-gcc-toolset-compatibility/38286")

    def install(self, spec, prefix):
      """ Create bash setup script in prefix."""

      # first, log spack version to build-out

      tty.msg('* **Spack:**', get_version())
      tty.msg('* **Python:**', platform.python_version())
      tty.msg('* **Platform:**', architecture.Arch(
          architecture.platform(), 'frontend', 'frontend'))


      specs = [spec]
      with spack.store.db.read_transaction():
               specs = [dep for _spec in specs
                        for dep in
                        _spec.traverse( order='post')]
               try: 
                   gcc_specs = [spack.cmd.disambiguate_spec(str(spec.compiler), None, first=True)]
                   gcc_specs = [dep for _spec in gcc_specs
                            for dep in
                            _spec.traverse( order='post')]
                   specs = specs + gcc_specs
               except:
                   tty.warn("No spec found for " + str(spec.compiler) + " Assuming it is a system compiler and not adding it to the setup.")
      env_mod = spack.util.environment.EnvironmentModifications()
      for _spec in specs:
          env_mod.extend(uenv.environment_modifications_for_spec(_spec))
          env_mod.prepend_path(uenv.spack_loaded_hashes_var, _spec.dag_hash())
      cmds = k4_generate_setup_script(env_mod)
      with open(os.path.join(prefix, "setup.sh"), "w") as f:
        f.write(cmds)
        try:
          symlink_path = os.environ.get("K4_LATEST_SETUP_PATH", "")
          if symlink_path:
              if not os.path.exists(os.path.dirname(symlink_path)):
                os.makedirs(os.path.dirname(symlink_path))
              if os.path.exists(symlink_path) or os.path.islink(symlink_path):
                os.remove(symlink_path)
              os.symlink(os.path.join(prefix, "setup.sh"), symlink_path)
        except:
          tty.warn("Could not create symlink")


   

    
