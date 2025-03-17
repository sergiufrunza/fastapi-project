import {useState} from 'react';
import {apiClient} from "../clients/apiClient.jsx";
import { useNavigate } from 'react-router-dom';

export function UploadPDF() {
    const [selectedFile, setSelectedFile] = useState(null);
    const navigate = useNavigate();

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file && file.type === 'application/pdf') {
            setSelectedFile(file);
        } else {
            setSelectedFile(null);
        }
    };

    const handleUpload = () => {
        const formData = new FormData();
        if (!selectedFile) {
            return
        }
        formData.append('file', selectedFile);
        apiClient.post('/files/upload', formData, {
            headers: {'Content-Type': 'multipart/form-data'}
        }).then(response => {
            if (response.data && response.data.id) {
                navigate(`/quiz/${response.data.id}`);
            }
        }).catch(error => {
        });
        setSelectedFile(null);
    };
    return (
        <div className="w-full max-w-lg flex flex-col gap-8">
            <label htmlFor="dropzone-file"
                   className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100">
                <div className="flex flex-col items-center justify-center pt-5 pb-6">
                    <svg className="w-8 h-8 mb-4 text-gray-500" aria-hidden="true"
                         xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                        <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round"
                              strokeWidth="2"
                              d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                    </svg>
                    <p className="mb-2 text-sm text-gray-500"><span
                        className="font-semibold">Click to upload</span> or drag and drop</p>
                    {selectedFile && <p className="text-xs text-gray-500 ">Selected file: {selectedFile.name}</p>}
                </div>
                <input id="dropzone-file" type="file" className="hidden" accept=".pdf" onChange={handleFileChange}/>
            </label>
            <button
                onClick={handleUpload}
                disabled={!selectedFile}
                className={`mt-4 w-full py-3  rounded-lg transition-colors duration-300 ${
                    selectedFile
                        ? 'bg-blue-600 hover:bg-blue-700 cursor-pointer text-white'
                        : 'bg-gray-400 cursor-not-allowed text-gray-700'
                }`}>
                Send File
            </button>
        </div>

    )
}