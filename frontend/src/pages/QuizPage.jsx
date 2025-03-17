import {Quiz} from "../components/Quiz.jsx";
import { useParams, useNavigate } from 'react-router-dom';
import {useEffect, useState} from 'react';
import {apiClient} from '../clients/apiClient';

export function QuizPage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [quizData, setQuizData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (!id) {
            navigate('/upload');
            return;
        }

        setLoading(true);
        apiClient.post(`/gpt/${id}`, {quiz: ""})
            .then(response => {
                setQuizData(response.data);
                setLoading(false);
            })
            .catch(error => {
                setLoading(false);
            });
    }, [id]);
    if (loading) {
        return <div className="grid place-items-center w-full h-full">
            <h2 className="text-center text-2xl/9 font-bold tracking-tight text-gray-900">
                Se încarcă...</h2>
        </div>;
    }
    return (
        <div className="grid place-items-center w-full h-full">
            {quizData ? <Quiz id={id} data={quizData} setQuizData={setQuizData}/> :
                <h2 className="text-center text-2xl/9 font-bold tracking-tight text-gray-900">Nu s-a putut încărca
                    quiz-ul</h2>}
        </div>
    );
}