import {Link} from "react-router-dom";


export function IndexPage() {
    return (
            <div className="text-center py-6 w-full h-full flex flex-col items-center justify-center">
                <Link to="/upload"
                      className="inline-flex justify-between items-center py-1 px-1 pr-4 mb-7 text-sm text-gray-700 bg-gray-100 rounded-full  hover:bg-gray-200 "
                      role="alert">
                                <span
                                    className="text-xs bg-blue-600 rounded-full text-white px-4 py-1.5 mr-3">New</span>
                    <span className="text-sm font-medium">Convert pdf to quiz</span>
                    <svg className="ml-2 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                         xmlns="http://www.w3.org/2000/svg">
                        <path fillRule="evenodd"
                              d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                              clipRule="evenodd"></path>
                    </svg>
                </Link>
                <h1 className="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 mx-auto max-w-4xl md:text-5xl lg:text-6xl">
                    Turn Any PDF into an Interactive Quiz Instantly!
                </h1>
                <p className="mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 ">Simply
                    upload your PDF file, and instantly generate a quiz of 5 engaging questions. Transform
                    your documents into interactive learning in seconds!</p>
                <Link to="/upload"
                      className=" mt-6 inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-blue-600 hover:bg-blue-700 focus:ring-4 ">
                    Get started
                    <svg className="ml-2 -mr-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                         xmlns="http://www.w3.org/2000/svg">
                        <path fillRule="evenodd"
                              d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                              clipRule="evenodd"></path>
                    </svg>
                </Link>
            </div>
    )
}